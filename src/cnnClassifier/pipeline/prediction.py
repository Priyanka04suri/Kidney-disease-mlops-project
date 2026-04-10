import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
from pathlib import Path

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
    
    def predict(self):
        # Get the directory where THIS FILE (prediction.py) is located
        # This gives: /path/to/KIDNEY-DISEASE-MLOPS-PROJECT/src/cnnClassifier/pipeline/
        current_dir = Path(__file__).resolve().parent
        
        # Go up 3 levels to reach project root
        # pipeline -> cnnClassifier -> src -> project_root
        project_root = current_dir.parent.parent.parent
        
        # Build path to model file
        model_path = project_root / "model" / "model.h5"
        
        # Debug: Print the path to verify
        print(f"Loading model from: {model_path}")
        print(f"File exists: {model_path.exists()}")
        
        # Load model
        model = load_model(str(model_path))

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