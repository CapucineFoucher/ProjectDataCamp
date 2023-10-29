from model import Model
import tensorflow as tf


# Create an instance of the model
model = Model()

model.create_model()

image_path = 'BACK/data/Test_Set/Test/1.png'  # Replace with the actual path to your image
prediction = model.predict(image_path)

print(f'Prediction for image A.png: Disease Risk = {prediction}')