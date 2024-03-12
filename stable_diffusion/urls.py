from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from .views import generate_txt2img

# router = routers.DefaultRouter()
# router.register(r'users', views.generate_txt2img, basename='user')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('txt2img', generate_txt2img, name='generate_txt2img'),
    path('img2img', generate_txt2img, name='generate_img2img'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
