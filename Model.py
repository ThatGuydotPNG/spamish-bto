import PIL
PIL.__version__
from PIL import Image
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

def detect_bird(path, model_path="keras_model.h5", labels_path="labels.txt"):
  # Disable scientific notation for clarity
  np.set_printoptions(suppress=True)

  # Load the model
  model = load_model(model_path, compile=False)

  # Load the labels
  class_names = open(labels_path, "r").readlines()

  # Create the array of the right shape to feed into the keras model
  # The 'length' or number of images you can put into the array is
  # determined by the first position in the shape tuple, in this case 1
  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

  # Replace this with the path to your image
  image = Image.open(path).convert("RGB")

  # resizing the image to be at least 224x224 and then cropping from the center
  size = (224, 224)
  image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

  # turn the image into a numpy array
  image_array = np.asarray(image)

  # Normalize the image
  normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

  # Load the image into the array
  data[0] = normalized_image_array

  # Predicts the model
  prediction = model.predict(data)
  index = np.argmax(prediction)
  class_name = class_names[index].strip()
  confidence_score = prediction[0][index]

  
  if class_name == "Pigeon":
    return class_name, confidence_score, "maíz, garbanzos, trigo, cebada, semillas, trigo sarraceno, mijo, guisantes, lentejas"
  elif class_name == "Sparrow":
    return class_name, confidence_score, "maíz partido, granos de cereales, avena, trigo, arroz e insectos secos"
  elif class_name == "Colibries":
    return class_name, confidence_score, "nectar, insectos secos, polen y savias"
  else:
    print("Class:", class_name)
    print("Confidence Score:", confidence_score)