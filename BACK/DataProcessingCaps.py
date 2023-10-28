import pandas as pd
import os
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import numpy as np


current_dir = os.getcwd()
df_val = pd.read_csv(current_dir + 'data/Evaluation_Set/RFMiD_Validation_Labels.csv')



evalDir = os.path.join(current_dir, 'data/Evaluation_Set')
trainDir = os.path.join(current_dir, 'data/Training_Set')
testDir = os.path.join(current_dir, 'data/Test_Set')



# Define data directories 
df_test = pd.read_csv(testDir+'/RFMiD_Testing_Labels.csv')
print(df_test.head())
df_train = pd.read_csv(trainDir+ '/RFMiD_Training_Labels.csv')
print(df_train.head())
df_val = pd.read_csv(current_dir + 'data/Evaluation_Set/RFMiD_Validation_Labels.csv')
print(df_val.head())

# Linking images to dataframe
images_test = []
images_train = []
images_val = []
# Load and store all images
for ID in df_test['ID']:
    image_test_path = os.path.join(testDir+'/Test', f'{ID}.png')
    image = Image.open(image_test_path)
    images_test.append(image)
for ID in df_train['ID']:
    image_train_path = os.path.join(trainDir+'/Training', f'{ID}.png')
    image = Image.open(image_train_path)
    images_train.append(image)
for ID in df_val['ID']:
    image_val_path = os.path.join(evalDir+'/Validation', f'{ID}.png')
    image = Image.open(image_val_path)
    images_val.append(image)


# Choose the image index you want to display
image_index = 2  # Change the index as needed
# Display the chosen image
plt.imshow(images_test[image_index-1])
plt.show()
# Display the chosen image
plt.imshow(images_train[image_index-1])
plt.show()
# Display the chosen image
plt.imshow(images_val[image_index-1])
plt.show()