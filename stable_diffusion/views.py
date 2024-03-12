
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from .api_request import StableDiffusionApiRequest

import logging

@api_view()
def generate_txt2img(request):
    """
        genereate txt2img with stable diffusion api
    """

    try:
        # comment:
        sd_request = StableDiffusionApiRequest()
        sd_request.schema.steps = 5
        sd_request.schema.prompt = "A cat 111"

        res = sd_request.txt2simg()
        # print(res['images'])
        # res.images = [f"data:image/png;base64,{img}" for img in res.images]

        return Response(res.images, status=status.HTTP_200_OK)
    except Exception as e:
        logging.error(f"ErrorAPI: {e}")
        raise APIException(code=status.HTTP_404_NOT_FOUND, detail=f"ErrorAPI: {e}")
    # end try


@api_view()
def generate_img2img(request):
    """
        genereate img2img with stable diffusion api
    """

    try:
        # comment:
        sd_request = StableDiffusionApiRequest()
        res = sd_request.img2img()
        return Response({"message": res})
    except Exception as e:
        raise e
    # end try
