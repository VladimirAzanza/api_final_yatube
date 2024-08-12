from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer
)
from .mixin import OnlyAuthorMixinViewSet
from posts.models import Follow, Group, Post


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


class FollowViewSet(ListCreateAPIView):
    serializer_class = FollowSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    pagination_class = None
    permission_classes = (IsAuthenticated,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
