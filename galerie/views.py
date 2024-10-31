from rest_framework import viewsets
from .models import Image
from .serializers import ImageSerializer
from PIL import Image as PilImage
from io import BytesIO
from django.core.files.base import ContentFile

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all().order_by('-upload_date')  # Ordre décroissant
    serializer_class = ImageSerializer

    def perform_create(self, serializer):
        image = serializer.save()
        self.create_thumbnail(image)

    def create_thumbnail(self, image):
        original_image = PilImage.open(image.image_file)
        thumbnail = original_image.resize((150, 150))
        thumb_io = BytesIO()
        thumbnail.save(thumb_io, format='JPEG')
        thumb_file = ContentFile(thumb_io.getvalue(), name=f'thumb_{image.image_file.name}')
        image.thumbnail.save(f'thumb_{image.image_file.name}', thumb_file)
        image.save()
