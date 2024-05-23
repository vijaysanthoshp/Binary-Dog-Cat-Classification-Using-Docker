# Intro

This repository contains a Flask web application that allows users to upload images and receive predictions on whether the image is of a cat or a dog. The application leverages a pre-trained deep learning model (in H5 format) to make these predictions. Additionally, the entire application is containerized using Docker, ensuring a consistent and reproducible environment.

# Features
 - User-friendly Interface: A simple web interface for uploading images.
 - Accurate Predictions: Utilizes a pre-trained model to predict if the uploaded image is of a cat or a dog.
 - Containerized Deployment: Dockerized application for easy setup and deployment.

# How It Works
 - Upload Image: Users can upload an image through the web interface.
 - Prediction: The uploaded image is passed to a pre-trained model which predicts whether the image is of a cat or a dog.
 - Result: The prediction result is displayed on the web interface.

## Create API : Flask

<p align="center">
<img src="./images/flask.png" alt="flask logo" width="350" height="100">
</p>

We are also using Flask-Uploads (or Flask-Reuploaded) which allows your application to flexibly and efficiently handle file uploading and serving the uploaded files.

[upload.py](./upload.py) contains the code responsible for running the API. It interacts with the [web page](./templates/upload.html) where the client will upload his image.

## Containerize : Docker

<p align="center">
<img src="./images/docker.png" alt="docker logo" width="350" height="100">
</p>

In short, Docker allows us to create reproducible environments. To do so for the API we've just created, we have to :

**1.** The first thing to do, obviously, is to [download and install Docker](https://www.docker.com/products/docker-desktop)

**2.** Create the [requirements.txt](./requirements.txt) in your main directory

**3.** Create a [Dockerfile](./Dockerfile) (without extension) which contains the instructions for building your Docker image

**4.** In a terminal, run the following command to build the Docker image:
  ```
  # docker build -t my-flask-app .
  ```

**5.** Run container in background and print container ID using:
```
# docker run -p 5000:5000 my-flask-app
```

Once this is running, you should be able to view your app running in your browser at
```
http://127.0.0.1:5000/upload
```


# Demo Video

https://github.com/vijaysanthoshp/Binary-Dog-Cat-Classification-Using-Docker/assets/143861101/a4b9dc42-1ea4-4aec-870b-03a090466523


# Acknowledgement and Links

h5 model link: https://huggingface.co/spaces/Sa-m/Dogs-vs-Cats/blob/main/best_model.h5

dockerhub link: https://hub.docker.com/repository/docker/vijaysanthoshp/flask_docker/general

# License
This project is licensed under the MIT License.


# Contact
For any inquiries or issues, please contact [vijaysanthoshpandiyaraj@gmail.com].


