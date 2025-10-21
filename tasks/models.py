from django.db import models
from authentification.models import User
import uuid
from django.utils.text import slugify


# Create your models here.


class Task(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Générer le slug à partir du titre
            self.slug = slugify(self.title)
            # S'assurer que le slug est unique
            slug_original = self.slug
            counter = 1
            while Task.objects.filter(slug=self.slug).exists():
                self.slug = f"{slug_original} - {counter}"
                counter += 1
        super().save(*args, **kwargs)
        

    def __str__(self):
        return self.title
    
