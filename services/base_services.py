from django.core.files.storage import FileSystemStorage
from mediaAI import settings

class BaseService():
    
    def __init__(self) -> None:
        self.fs = FileSystemStorage()
        self.settings = settings