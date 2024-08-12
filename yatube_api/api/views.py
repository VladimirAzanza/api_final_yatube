from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import CommentSerializer, GroupSerializer, PostSerializer
from .mixin import OnlyAuthorMixinViewSet
from posts.models import Group, Post


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = None


class PostViewSet(OnlyAuthorMixinViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(OnlyAuthorMixinViewSet):
    serializer_class = CommentSerializer
    pagination_class = None

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=self.get_post()
        )
