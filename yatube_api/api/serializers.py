from posts.models import Comment, Group, Post, User
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = (
            'id',
            'title',
            'slug',
            'description'
        )


class PostSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(
        required=False,
        queryset=Group.objects.all()
    )
    author = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Post
        fields = (
            'id',
            'text',
            'author',
            'image',
            'group',
            'pub_date'
        )


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Comment
        fields = (
            'id',
            'author',
            'post',
            'text',
            'created'
        )
        read_only_fields = ('post',)
