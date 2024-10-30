from celery import shared_task
from PIL import Image as PILImage
from django.core.files.base import ContentFile
from io import BytesIO
from .models import Image


@shared_task
def generate_thumbnail(image_id):
    try:
        image_instance = Image.objects.get(id=image_id)
        pil_image = PILImage.open(image_instance.image)
        pil_image.thumbnail((200, 200))

        thumb_io = BytesIO()
        pil_image.save(thumb_io, format='JPEG')
        image_instance.thumbnail.save(f'thumb_{image_instance.image.name}', ContentFile(thumb_io.getvalue()),
                                      save=False)
        image_instance.save()
    except Image.DoesNotExist:
        pass
