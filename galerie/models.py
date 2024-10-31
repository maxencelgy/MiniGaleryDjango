from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=100)
    image_file = models.ImageField(upload_to='uploads/')  # Vérifiez que ce champ existe
    upload_date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='uploads/thumbnails/', blank=True, null=True)

    def __str__(self):
        return self.title
