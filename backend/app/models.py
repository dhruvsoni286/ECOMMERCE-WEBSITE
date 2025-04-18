from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='item_images/', null=True, blank=True)

    def __str__(self):
        return self.name
