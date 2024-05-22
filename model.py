import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.vgg19 import preprocess_input
import numpy as np

# Load the pre-trained model
model = load_model('./weights/best_model.h5', compile=False)

def process_image(image):
    '''
    Make an image ready-to-use by VGG19
    '''
    # Convert the image to an array and expand dimensions to match the model's input shape
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    # Preprocess the image for the VGG19 model
    image = preprocess_input(image)
    return image

def predict_class(image):
    '''
    Predict and render the class of a given image 
    '''
    # Predict the probability across all output classes
    yhat = model.predict(image)
    # Interpret the prediction
    if yhat[0][0] > yhat[0][1]:
        prob = yhat[0][0]
        prediction = 'cat'
    else:
        prob = yhat[0][1]
        prediction = 'dog'
    percentage = '%.2f%%' % (prob * 100)
    return prediction, percentage

if __name__ == '__main__':
    # For testing purposes
    # Load an image from file
    image = load_img('../image.jpg', target_size=(224, 224))
    image = process_image(image)
    prediction, percentage = predict_class(image)
    print(prediction, percentage)
