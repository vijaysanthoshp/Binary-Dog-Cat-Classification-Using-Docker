# ML-in-production

In this tutorial we will try to walk together through all the building blocks of a Machine/Deep Learning project in production, i.e. a model that people can actually interact with

As a case study, we’ll be creating a web interface for image recognition using the pretrained model VGG19.

You can check the detailed explanation on the article I wrote in Towards Data Science [here](https://towardsdatascience.com/machine-learning-in-production-keras-flask-docker-and-heroku-933b5f885459)


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

## Deploy : Heroku

<p align="center">
<img src="./images/heroku.png" alt="heroku logo" width="350" height="100">
</p>

Thanks to [Heroku](https://www.heroku.com/) we will be able to deploy our application in the Cloud

**1.** Create a new [Heroku account](https://signup.heroku.com/) if you don’t have one. Then download Heroku [Command Line Interface (CLI)](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) which makes it easy to create and manage your Heroku apps directly from the terminal.

**2.** Login to your Heroku account using `# heroku login`

**3.** Log in to Container Registry: `# heroku container:login`

**4.** Create a new Heroku app: `# heroku create <app-name>`

**5.** Build the image based on your Dockefile and push it to this particular app in Heroku `# heroku container:push web --app <app-name>`

**6.** You can finally open up your Heroku application through the command `# heroku open --app <app-name>`

# Demo Video

https://github.com/vijaysanthoshp/Binary-Dog-Cat-Classification-Using-Docker/assets/143861101/a4b9dc42-1ea4-4aec-870b-03a090466523


# Acknowledgement and Links

h5 model link: https://huggingface.co/spaces/Sa-m/Dogs-vs-Cats/blob/main/best_model.h5

dockerhub link: https://hub.docker.com/repository/docker/chanjhana/cat_dog_classifier/general

# Contact

