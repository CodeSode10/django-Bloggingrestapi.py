from rest_framework import serializers
from .models import *

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = "__all__"

class BlogPostSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = BlogPost
        fields = ["id", "user", "title", "content", "created_at", "updated_at", "images",
                  "uploaded_images"]

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        blogpost = BlogPost.objects.create(**validated_data)

        for image in uploaded_images:
            Images.objects.create(post=blogpost, image=image)

        return blogpost
