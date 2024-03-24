from services.yolo_service import YoloMediaService
from ultralytics import SAM
from ultralytics import FastSAM
from ultralytics.models.fastsam import FastSAMPrompt

class YoloSamMediaService(YoloMediaService):

    def __init__(self, model: str = 'sam_l.pt'):
        self.model = SAM(model)
        
    
    def detect_objects_from_url(self, url):
        predicted_results = self.model.predict(url,labels=['person'])
        return predicted_results
    
    
    
    
class YoloFastSamMediaService(YoloMediaService):

    def __init__(self, model: str = 'FastSAM-x.pt'):
        # self.model = FastSAM(model)
        pass
    
    def detect_objects_from_url(self, url):
        # Run inference on an image
        self.model = FastSAM('FastSAM-x.pt')
        everything_results = self.model.predict(url, device='cpu')

        # Prepare a Prompt Process object
        prompt_process = FastSAMPrompt(url, everything_results, device='cpu')
        
        # Everything prompt
        # ann = prompt_process.everything_prompt()

        # Bbox default shape [0,0,0,0] -> [x1,y1,x2,y2]
        # ann = prompt_process.box_prompt(bbox=[200, 200, 300, 300])

        # Text prompt
        ann = prompt_process.text_prompt(text='person')
        
        # get person mask with prompt process
        
        print("ann", ann)
        # everything_results
        return ann