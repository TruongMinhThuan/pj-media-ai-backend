from django.core.files.storage import FileSystemStorage
from mediaAI import settings
from django.http import HttpRequest


class BaseService():

    def __init__(self) -> None:
        self.fs = FileSystemStorage()
        self.settings = settings

    def build_url(self, request: HttpRequest, path: str) -> str:
        
        # build http url hosting example http://localhost:8000
        return request.build_absolute_uri(f'{settings.MEDIA_URL}{path}')
        