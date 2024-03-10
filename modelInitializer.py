from ultralytics import YOLO

def getModel():
    
    # Load the model
    # Use better .pt files/models if you need customisation

    model = YOLO('yolov8n-pose.pt')  # load an official model
    return model

model = getModel()