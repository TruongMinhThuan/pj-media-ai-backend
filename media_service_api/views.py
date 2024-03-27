# Create your views here.
from requests import Request
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
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


@swagger_auto_schema(
    request_body=serializers.RemoveBackgroundRequestSerializer,
    method='post',
    responses={200: serializers.RemoveBackgroundResponseSerializer}
)
@api_view(['POST'])
@parser_classes([MultiPartParser])
def remove_image_background(request: Request, *args, **kwargs):
    print("image_file", request.data['image_file'])

    request_serializer = serializers.RemoveBackgroundRequestSerializer(
        data=request.data)
    
    if request_serializer.is_valid():
        image_file = request_serializer.validated_data['image_file']

        img_service = ImageServices()
        file_path = img_service.fs.save('upload_images/image.jpg', image_file)

        processed_image = img_service.remove_image_background(f'{file_path}')

        response_serializer = serializers.RemoveBackgroundResponseSerializer(data={
            'input_image_url': img_service.build_url(request, file_path),
            'processed_image_url': img_service.build_url(request, processed_image)
        })
        
        if response_serializer.is_valid():
            return Response({"message": "Saved Image", "data": response_serializer.data})
        else:
            return Response({"message": "Saved Image Failed"})


    return Response({"message": "Saved Image Failed"})
