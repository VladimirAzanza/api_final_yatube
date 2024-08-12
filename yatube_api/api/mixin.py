from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet


class OnlyAuthorMixinViewSet(ModelViewSet):
    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied(
                'У вас недостаточно прав для выполнения данного действия.'
            )
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied(
                'У вас недостаточно прав для выполнения данного действия.'
            )
        super().perform_destroy(instance)
