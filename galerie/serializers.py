from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "title", "image_file", "upload_date", "thumbnail"]
        read_only_fields = ["id", "thumbnail"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if self.context.get("request").method == "POST":
            representation.pop("id", None)
            representation.pop("thumbnail", None)

        return representation
