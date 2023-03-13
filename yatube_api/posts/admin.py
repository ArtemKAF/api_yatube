from django.contrib import admin

from .models import Comment, Follow, Group, Post


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'post', 'author', 'text', 'created',)
    search_fields = ('text',)
    list_filter = ('author',)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'slug',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('description',)
    list_filter = ('title',)


class FollowAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'following',)
    search_fields = ('following',)
    list_filter = ('user',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'group', 'text', 'pub_date',)
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('author', 'group',)
    empty_value_display = '-пусто-'


admin.site.register(Comment, CommentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Post, PostAdmin)
