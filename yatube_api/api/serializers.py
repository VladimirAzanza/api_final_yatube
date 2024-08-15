from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .base64_image_field import Base64ImageField
from posts.models import Comment, Follow, Group, Post


User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    image = Base64ImageField(required=False)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('pub_date',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(
    #    slug_field='username',
    #    read_only=True,
    #    default=serializers.CurrentUserDefault()
    # )
    # Вы просили не переопределять поле, но если убрать это - user: user.id
    # А тесты не проходят: "AssertionError: Проверьте, что при GET-запросе
    # авторизованного пользователя к `/api/v1/follow/` в поле `user` каждого
    # из объектов подписки содержится корректный `username` пользователя.

    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        required=True
    )

    class Meta:
        exclude = ('id',)
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]

    def validate_following(self, value):
        if value == self.context['request'].user:
            raise serializers.ValidationError(
                'Вы не можете быть своим собственным подписдчиком.'
                'Введите данные правильно.'
            )
        return value
