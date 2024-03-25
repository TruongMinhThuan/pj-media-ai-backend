from ultralytics import YOLO

from services.base_services import BaseService
import torch
from PIL import Image
from torchvision.utils import save_image
from datetime import datetime

class YoloMediaService(BaseService):

    def __init__(self, model='models/yolov8n-seg.pt') -> None:
        super().__init__()
        self.model = YOLO(model)

    def detect_objects(self, image_path):
        return self.model(image_path)

    def detect_objects_bulk(self, folder_path):
        return self.model(folder_path)

    def detect_objects_from_url(self, url):
        print("model informaton", self.model.info())
        results = self.model.predict(url,classes=[0])  # predict on an image
        return results

    def detect_objects_from_url_bulk(self, urls):
        return self.model(urls)

    def save_mask_objects(self, mask_data):

        mask = torch.any(mask_data, dim=0).int() * 255

        # # Read image numpy array with Image
        img = Image.fromarray(mask.cpu().numpy())
        
        #Convert image to 'L' mode
        img = img.convert('L')

        # # Save image
        img_name = datetime.now().strftime("mask_%Y%m%d%H%M%S") + '.jpg'
        
        img.save(img_name)


