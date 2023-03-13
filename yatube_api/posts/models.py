from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True,
        db_index=True,
        unique=True,
    )
    post = models.ForeignKey(
        'Post',
        verbose_name='Публикация',
        on_delete=models.CASCADE,
    )
    text = models.TextField(
        verbose_name='Текст комментария',
    )

    class Meta:
        default_related_name = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Follow(models.Model):
    following = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='following',
    )
    user = models.ForeignKey(
        User,
        verbose_name='Подписчик',
        on_delete=models.CASCADE,
        related_name='follower',
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=('following', 'user'),
                name='%(app_label)s_%(class)s_unique_relationships',
            ),
            models.CheckConstraint(
                check=(models.Q(user__gt=models.F('following'))
                       | models.Q(user__lt=models.F('following'))),
                name='%(app_label)s_%(class)s_prevent_following_yourself',
            ),
        ]

    def __str__(self):
        return f'{self.user} подписан на {self.following}'


class Group(models.Model):
    description = models.TextField(
        verbose_name='Описание',
    )
    slug = models.SlugField(
        verbose_name='Адрес',
        db_index=True,
        unique=True,
    )
    title = models.CharField(
        verbose_name='Название сообщества',
        max_length=200,
    )

    class Meta:
        verbose_name = 'Сообщество'
        verbose_name_plural = 'Сообщества'

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
    )
    group = models.ForeignKey(
        Group,
        verbose_name='Сообщество',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    image = models.ImageField(
        upload_to='posts/',
        verbose_name='Изображение',
        null=True,
        blank=True,
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )
    text = models.TextField(
        verbose_name='Текст',
    )

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        default_related_name = 'posts'

    def __str__(self):
        return self.text
