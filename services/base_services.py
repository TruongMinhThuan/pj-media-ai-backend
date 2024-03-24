from django.core.files.storage import FileSystemStorage


class BaseService():
    
    def __init__(self) -> None:
        self.fs = FileSystemStorage()