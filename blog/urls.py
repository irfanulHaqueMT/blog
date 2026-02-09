from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, TagViewSet, ContactMessageView, CurrentUserView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('contact/', ContactMessageView.as_view(), name='contact'),
    path('me/', CurrentUserView.as_view(), name='current_user'),
]
