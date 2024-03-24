from .base_services import BaseService
from PIL import Image
from rembg import remove as remove_img_background
import urllib3
import urllib.request
import os
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from pathlib import Path


class ImageServices(BaseService):

    def __init__(self) -> None:
        super().__init__()
        self.upload_folder_default = self.settings.MEDIA_ROOT + '/uploads_images'

    def flip_image(self, image):
        return Image.open(image).transpose(Image.FLIP_LEFT_RIGHT)

    def rotate_image(self, image, degrees):
        return Image.open(image).rotate(degrees)

    def resize_image(self, image, size):
        return Image.open(image).resize(size)

    def remove_image(self, image_path):
        os.remove(image_path)

    def resize_image_bulk(self, folder_path, size: tuple[int, int] | None = (768, 768)):

        for file in Path(folder_path).glob('*.jpg'):
            input_path = str(file)
            output_path = str(file.parent / (file.stem + "-resized.jpg"))
            # output_path = input_path

            with open(input_path, 'rb') as i:
                with open(output_path, 'wb') as o:
                    img = Image.open(i)
                    img.convert('RGB')
                    img_resized = img.resize(size)
                    img_resized.save(o)

            self.remove_image(input_path)

        return folder_path

    def flip_image_bulk(self, folder_path):

        for file in Path(folder_path).glob('*.jpg'):
            input_path = str(file)
            output_path = str(file.parent / (file.stem + "-flipped.jpg"))

            with open(input_path, 'rb') as i:
                with open(output_path, 'wb') as o:
                    img = Image.open(i)
                    img.convert('RGB')
                    img_flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
                    img_flipped.save(o)

        return folder_path

    def duplicate_image_bulk(self, folder_path):

        for file in Path(folder_path).glob('*.jpg'):
            input_path = str(file)
            output_path = str(file.parent / (file.stem + "-duplicated.jpg"))

            with open(input_path, 'rb') as i:
                with open(output_path, 'wb') as o:
                    img = Image.open(i)
                    img.convert('RGB')
                    img.save(o)

        return folder_path

    def save_image(self, image, path):
        return Image.open(image).save(path)

    def show_image(self, image):
        return Image.open(image).show()

    def close_image(self, image):
        return Image.open(image).close()

    def get_image_size(self, image):
        return Image.open(image).size

    def get_image_format(self, image):
        return Image.open(image).format

    def remove_image_background(self, image_path: str | None = None):

        if image_path:
            with open(image_path, 'rb') as i:
                with open(image_path.replace(".jpg", ".out.jpg"), 'wb') as o:
                    input = i.read()
                    output = remove_img_background(input)
                    o.write(output)
                    

    def remove_image_background_bulk(self, folder_path: str | None = None):

        for file in Path(folder_path).glob('*.jpg'):
            input_path = str(file)
            output_path = str(file.parent / (file.stem + ".out.jpg"))

            with open(input_path, 'rb') as i:
                with open(output_path, 'wb') as o:
                    input = i.read()
                    output = remove_img_background(input)
                    o.write(output)

    def get_unique_datetime_img_name(self, extension='.jpg'):
        dt_str = f'{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}{extension}'
        print("dt_str: ", dt_str)
        return dt_str

    def save_image_bulks_from_image_url(self, image_url_list, folder_path: str | None = None):

        for image_url in image_url_list:
            storage = FileSystemStorage(location=folder_path)
            storage.save(self.get_unique_datetime_img_name(),
                         urllib.request.urlopen(image_url))

        return folder_path

    def create_folder_if_not_exists(self, folder_path):
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        return folder_path
