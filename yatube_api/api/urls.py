from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api_v1'

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, basename='post')
router_v1.register('groups', GroupViewSet, basename='group')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment_post'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/follow/', FollowViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='follow'),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt'))
]
