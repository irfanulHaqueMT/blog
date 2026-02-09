from rest_framework import serializers
from .models import Post, Tag, ContactMessage
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), source='tags', write_only=True, many=True, required=False
    )

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'author', 'content', 'excerpt', 
            'cover_image', 'tags', 'tag_ids', 'published', 
            'created_at', 'updated_at', 'reading_time'
        ]
        read_only_fields = ['slug', 'reading_time', 'author']

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'message', 'created_at']
