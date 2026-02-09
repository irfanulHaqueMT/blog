from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from .models import Post, Tag, ContactMessage
from .serializers import PostSerializer, TagSerializer, ContactMessageSerializer, UserSerializer
from django.shortcuts import get_object_or_404

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(published=True)
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Post.objects.all()
        return Post.objects.filter(published=True)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'

class ContactMessageView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CurrentUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
