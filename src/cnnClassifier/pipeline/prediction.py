import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
from pathlib import Path

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
    
    def predict(self):
        # Hardcoded path for your project structure
        model_path = "KIDNEY-DISEASE-MLOPS-PROJECT/model/model.h5"
        
        # Alternative: If you're already in the project directory
        # model_path = "model/model.h5"
        
        print(f"Loading model from: {model_path}")
        print(f"File exists: {os.path.exists(model_path)}")
        
        # Load model
        model = load_model(model_path)

        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Tumor'
            return [{"image": prediction}]
        else:
            prediction = 'Normal'
            return [{"image": prediction}]