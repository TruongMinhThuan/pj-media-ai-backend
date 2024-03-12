from django.contrib import admin

# Register your models here.

from .models import BrandingCategories, BrandingMediaImage

admin.site.register(BrandingCategories)
admin.site.register(BrandingMediaImage)
