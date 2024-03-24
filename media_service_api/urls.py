from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# router = routers.DefaultRouter()
# router.register(r'users', views.generate_txt2img, basename='user')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('mask', view=views.generate_image_mask, name='generate_mask'),
    path('rm_background', view=views.remove_image_background, name='remove_background'),

]

