from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import CommentsViewSet, FollowsViewSet, GroupsViewSet, PostsViewSet

router = SimpleRouter()
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentsViewSet,
    basename='comments'
)
router.register('follow', FollowsViewSet, basename='follow')
router.register('groups', GroupsViewSet)
router.register('posts', PostsViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
