import requests
from rest_framework.response import Response

from django.http import HttpResponse, JsonResponse
from rest_framework.exceptions import APIException
from .schema import StableDiffusionBaseSchema, StableDiffusionImg2ImgSchema, StableDiffusionTxt2ImgSchema, StableDiffusionResponseSchema
# get status code from rest_framework.response import Response
from rest_framework import status


class ApiRequestBase:
    def __init__(self):
        pass

    def __get_headers(self):
        return {
            "X-Api-Key": "Secret",

        }

    def __get_url(self, endpoint: str):
        return f"http://127.0.0.1:7861/{endpoint}"

    def post(self, endpoint: str, data: dict):
        try:
            # comment:
            headers = self.__get_headers()
            url = self.__get_url(endpoint)
            response = requests.post(url, headers=headers, json=data)

            if response.status_code != 200:
                raise APIException(code=response.status_code,
                                   detail=response.json())

            return response.json()

        except Exception as e:

            raise APIException(
                code=status.HTTP_404_NOT_FOUND, detail=f"Error: {e}")
        # end try


class StableDiffusionApiRequest(ApiRequestBase):
    def __init__(self):
        super().__init__()
        self.schema = StableDiffusionTxt2ImgSchema()

    def txt2img(self) -> StableDiffusionResponseSchema:

        res = self.post("sdapi/v1/txt2img", self.schema.model_dump())
        return StableDiffusionResponseSchema(**res)
    
    def img2img(self):
        res = self.post("sdapi/v1/img2img", self.schema.model_dump())

        return StableDiffusionResponseSchema(
            images=res["images"], message=res["message"], info=res["info"])

        