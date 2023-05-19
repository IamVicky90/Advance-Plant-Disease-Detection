# Plant-Disease-Prediction-model based on Convolutional Neural Network.
## Table of Contents.
  * [Demo](#demo)
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Technical Aspect](#technical-aspect)
  * [Installation](#installation)
  * [Run](#run)
  * [Directory Tree](#directory-tree)
  * [Libraries](#libraries)
  
  ## Demo
  Link. (Deployment Link is on progress...).
  
 
 __Frontent based on html, css.__
  
  ![error check your internet](https://github.com/IamVicky90/Plant-Disease-Prediction/blob/main/Images/1.PNG)
  
  
  __Prediction Button where you drop your image.__
  
  ![error check your internet](https://github.com/IamVicky90/Plant-Disease-Prediction/blob/main/Images/Capture.PNG)
  
 
 __Final result with some advise that how to cure the infected Plant.__
  
  ![error check your internet](https://github.com/IamVicky90/Plant-Disease-Prediction/blob/main/Images/3.PNG)
  
  ## Overview
This is a simple image classification Flask app trained on the top of Keras API. The trained model (`Plant-Disease-Prediction/Model/Various Plant Disease Detection Model1.h5`) takes an image (from Plant Disease) as an input and predict the class of image from __diseased cotton leaf, diseased cotton plant, fresh cotton leaf, fresh cotton plant, Pepper bell Bacterial spot, Pepper bell healthy, Potato Early blight, Potato healthy, Potato Late blight, Tomato Target Spot, Tomato Tomato mosaic virus, Tomato Tomato YellowLeaf Curl Virus, Tomato Bacterial spot, Tomato Early blight, Tomato healthy, Tomato Late blight, Tomato Leaf Mold, Tomato Septoria leaf spot, Tomato Spider mites Two spotted spider mite__ denomination.

## Motivation
What could be a perfect way to utilize unfortunate lockdown period? Like most of you, I spend my time in cooking, Netflix, coding and reading some latest research papers on weekends. This idea came into my mind when I read some research papers and by seeing the Kaggle compititions on Plant Disease Detection then I goto my village and see that how the farmers were seeing at the plants for different diseases. They were paying high fees to the plant disease specialists. So I utilize my best knowledge to overcome their expenses. 

## Technical Aspect
This project is divided into two part:
1. Training a deep learning model using Keras and by [.ipynb file](https://github.com/IamVicky90/Plant-Disease-Prediction/blob/main/.ipynb%20notebooks/Plant%20Disease%20Detection.ipynb).
2. Building and hosting a Flask web app on Heroku(it's not done yet).

## Installation
The Code is written in Python 3.7. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [downloading it](https://github.com/IamVicky90/Plant-Disease-Prediction/archive/main.zip):
```bash
pip install -r requirements.txt
```
## Run
To run the app in a local machine, shoot this command in the project directory:
__Run the follwing command after installing requirements.txt__
```bash
python app.py
```
## Directory Tree 
```
├── .ipynb notebooks
│   ├── .ipynb_checkpoints
│   ├── Plant Disease Detection.ipynb
│   ├── Predictions on Test data and classification Report.ipynb
│   └── debug.log
├── Images
│   ├── 1.PNG
│   ├── 2.PNG
│   ├── capture.PNG
├── Model
│   ├── Various Plant Disease Detection Model1.h5
├── Static
│   ├── Cotton Disease Images
│   ├── Images
│   ├── User Upload

├── Various Plant Disesse Detection Prediction DataSet
│   ├── Test
    │   ├── diseased cotton leaf
    │   ├── diseased cotton plant
    │   ├── fresh cotton leaf
    │   ├── fresh cotton plant
    │   ├── Pepper bell Bacterial spot
    │   ├── Pepper bell healthy
    │   ├── Potato Early blight
    │   ├── Potato healthy
    │   ├── Potato Late blight 
    │   ├── Tomato Target Spot 
    │   ├── Tomato Tomato mosaic virus
    │   ├── Tomato Tomato YellowLeaf Curl Virus
    │   ├── Tomato Bacterial spot
    │   ├── Tomato Early blight
    │   ├── Tomato healthy
    │   ├── Tomato Late blight
    │   ├── Tomato Leaf Mold
    │   ├── Tomato Septoria leaf spot
    │   ├── Tomato Spider mites Two spotted spider mite
│   ├── Train
    │   ├── diseased cotton leaf
    │   ├── diseased cotton plant
    │   ├── fresh cotton leaf
    │   ├── fresh cotton plant
    │   ├── Pepper bell Bacterial spot
    │   ├── Pepper bell healthy
    │   ├── Potato Early blight
    │   ├── Potato healthy
    │   ├── Potato Late blight 
    │   ├── Tomato Target Spot 
    │   ├── Tomato Tomato mosaic virus
    │   ├── Tomato Tomato YellowLeaf Curl Virus
    │   ├── Tomato Bacterial spot
    │   ├── Tomato Early blight
    │   ├── Tomato healthy
    │   ├── Tomato Late blight
    │   ├── Tomato Leaf Mold
    │   ├── Tomato Septoria leaf spot
    │   ├── Tomato Spider mites Two spotted spider mite
│   ├── Val
    │   ├── diseased cotton leaf
    │   ├── diseased cotton plant
    │   ├── fresh cotton leaf
    │   ├── fresh cotton plant
    │   ├── Pepper bell Bacterial spot
    │   ├── Pepper bell healthy
    │   ├── Potato Early blight
    │   ├── Potato healthy
    │   ├── Potato Late blight 
    │   ├── Tomato Target Spot 
    │   ├── Tomato Tomato mosaic virus
    │   ├── Tomato Tomato YellowLeaf Curl Virus
    │   ├── Tomato Bacterial spot
    │   ├── Tomato Early blight
    │   ├── Tomato healthy
    │   ├── Tomato Late blight
    │   ├── Tomato Leaf Mold
    │   ├── Tomato Septoria leaf spot
    │   ├── Tomato Spider mites Two spotted spider mite

├── templates
│   ├── index.html
│   ├── error.html
│   ├── diseased cotton leaf.html
│   ├── diseased cotton plant.html
│   ├── fresh cotton leaf.html
│   ├── fresh cotton plant.html
│   ├── Pepper bell Bacterial spot.html
│   ├── Pepper bell healthy.html
│   ├── Potato Early blight.html
│   ├── Potato healthy.html
│   ├── Potato Late blight.html
│   ├── Tomato Target Spot.html
│   ├── Tomato Tomato mosaic virus.html
│   ├── Tomato Tomato YellowLeaf Curl Virus.html
│   ├── Tomato Bacterial spot.html
│   ├── Tomato Early blight.html
│   ├── Tomato healthy.html
│   ├── Tomato Late blight.html
│   ├── Tomato Leaf Mold.html
│   ├── Tomato Septoria leaf spot.html
│   ├── Tomato Spider mites Two spotted spider mite.html
├── Procfile
├── README.md
├── app.py
├── requirements.txt
```
## Libraries
also mentioned in [requirements.txt](https://github.com/IamVicky90/Plant-Disease-Prediction/blob/main/requirements.txt)
```
* absl-py==0.11.0
* astunparse==1.6.3
* cached-property==1.5.2
* cachetools==4.2.0
* certifi==2020.12.5
* chardet==4.0.0
* click==7.1.2
* Flask==1.1.2
* flatbuffers==1.12
* gast==0.3.3
* google-auth==1.24.0
* google-auth-oauthlib==0.4.2
* google-pasta==0.2.0
* grpcio==1.32.0
* h5py==2.10.0
* idna==2.10
* importlib-metadata==3.3.0
* itsdangerous==1.1.0
* Jinja2==2.11.2
* Keras==2.4.3
* Keras-Preprocessing==1.1.2
* Markdown==3.3.3
* MarkupSafe==1.1.1
* numpy==1.19.4
* oauthlib==3.1.0
* opt-einsum==3.3.0
* protobuf==3.14.0
* pyasn1==0.4.8
* pyasn1-modules==0.2.8
* PyYAML==5.3.1
* requests==2.25.1
* requests-oauthlib==1.3.0
* rsa==4.6
* scipy==1.5.4
* six==1.15.0
* tensorboard==2.4.0
* tensorboard-plugin-wit==1.7.0
* tensorflow==2.4.0
* tensorflow-estimator==2.4.0
* termcolor==1.1.0
* typing-extensions==3.7.4.3
* urllib3==1.26.2
* Werkzeug==1.0.1
* wincertstore==0.2
* wrapt==1.12.1
* zipp==3.4.0 
```

