from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class BrandingCategories(models.Model):
    category = models.CharField(max_length=100)
    image_url = models.ImageField(upload_to='branding_categories', default='branding_categories/default.jpg',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.category
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_at <= now
    
    
    
class BrandingMediaImage(models.Model):
    category = models.ForeignKey(BrandingCategories, on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to='branding_media_images', default='branding_media_images/default.jpg',null=True, blank=True)
    prompt_text = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.prompt_text
    
