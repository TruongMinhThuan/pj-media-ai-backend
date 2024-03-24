# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from services.yolo_service import YoloMediaService
from services.yolo_sam_service import YoloSamMediaService, YoloFastSamMediaService
from services.image_service import ImageServices
from . import serializers
from drf_yasg.utils import swagger_auto_schema

from rest_framework.decorators import parser_classes
from drf_yasg import openapi


@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})


@api_view()
def generate_image_mask(request):

    img_service = YoloMediaService()

    res = img_service.detect_objects_from_url(
        'https://i.pinimg.com/564x/24/5b/ea/245beae2b5ecc7c84bde15f5a2a9c6c5.jpg')

    for result in res:
        boxes = result.boxes  # Boxes object for bounding box outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs  # Probs object for classification outputs
        # result.show()  # display to screen
        # result.save(filename='result.jpg')  # save to disk
        # print('masks:', masks[0])
        # img_service.save_mask_objects(masks[0].data)

    res_data = res[0]
    print('res:', res_data.masks.data)

    img_service.save_mask_objects(res_data.masks.data)

    return Response({"message": "Hello, world!"})

# add swagger decorator

from rest_framework.parsers import JSONParser, MultiPartParser, FormParser


@swagger_auto_schema(
    request_body=serializers.RemoveBackgroundRequestSerializer,
    method='post',
)
@api_view(['POST'])
@parser_classes([JSONParser,MultiPartParser,FormParser])
def remove_image_background(request):

    img_service = YoloSamMediaService()

    res = img_service.detect_objects_from_url(
        'https://i.pinimg.com/564x/24/5b/ea/245beae2b5ecc7c84bde15f5a2a9c6c5.jpg')

    for result in res:
        boxes = result.boxes
