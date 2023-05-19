#Import necessary libraries
from flask import Flask, render_template, request
 
import numpy as np
import os
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
 
#load model
model=load_model("Model/Various Plant Disease Detection Model1.h5")

print('@@ Model loaded')


def pred_plant_dieas(plant):
  test_image = load_img(plant, target_size = (150, 150)) # load image 
  print("@@ Got Image for prediction")
  test_image = img_to_array(test_image)/255 
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
   
  result = model.predict(test_image).round(3) 
  print('@@ Raw result = ', result)
   
  pred = np.argmax(result) 
 
  if pred == 0:
    return "Pepper bell Bacterial_spot", 'Pepper__bell___Bacterial_spot.html' 
  elif pred == 1:
      return 'Pepper bell healthy', 'Pepper__bell___healthy.html' 
  elif pred == 2:
      return 'Potato Early blight', 'Potato___Early_blight.html'  
  elif pred == 3:
      return 'Potato Late blight', 'Potato___Late_blight.html'  
  elif pred==4:
    return "Potato healthy", 'Potato___healthy.html' 
  elif pred==5:
    return "Tomato Bacterial spot", 'Tomato_Bacterial_spot.html' 
  elif pred==6:
    return "Tomato Early blight", 'Tomato_Early_blight.html' 
  elif pred==7:
    return "Tomato Late blight", 'Tomato_Late_blight.html' 
  elif pred==8:
    return "Tomato Leaf Mold", 'Tomato_Leaf_Mold.html' 
  elif pred==9:
    return "Tomato Septoria leaf spot", 'Tomato_Septoria_leaf_spot.html' 
  elif pred==10:
    return "Tomato Spider mites Two spotted spider mite", 'Tomato_Spider_mites_Two_spotted_spider_mite.html' 
  elif pred==11:
    return "Tomato Target Spot", 'Tomato__Target_Spot.html' 
  elif pred==12:
    return "Tomato Yellow Leaf Curl Virus", 'Tomato__Tomato_YellowLeaf__Curl_Virus.html' 
  elif pred==13:
    return "Tomato_mosaic_virus", 'Tomato__Tomato_mosaic_virus.html' 
  elif pred==14:
    return "Tomato healthy", 'Tomato_healthy.html' 
  elif pred==15:
    return "Diseased cotton leaf", 'diseased_cotton_leaf.html' 
  elif pred==16:
    return "Diseased cotton plant", 'diseased_cotton_plant.html' 
  elif pred==17:
    return "Fresh cotton leaf", 'fresh_cotton_leaf.html' 
  elif pred==18:
    return "Fresh cotton plant", 'fresh_cotton_plant.html' 
  else:
    return "An unknown error has been occured", 'error.html'

     





# Create flask instance
app = Flask(__name__)
 
# render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
  # return("Hellow World")
  return render_template("index.html")
@app.route("/about", methods=['GET', 'POST'])
def about():
  # return("Hellow World")
  return render_template("about.html")
@app.route("/services", methods=['GET', 'POST'])
def services():
  # return("Hellow World")
  return render_template("services.html")
@app.route("/contact", methods=['GET', 'POST'])
def contact():
  # return("Hellow World")
  return render_template("contact.html")
     
  
# get input image from client then predict class and render respective .html page for solution
@app.route("/predict", methods = ['GET','POST'])
def predict():

  if request.method == 'POST':
    file = request.files['image'] # fet input
    filename = file.filename        
    print("@@ Input posted = ", filename)
    file_path = os.path.join('static','user_upload', filename)
    file.save(file_path)
 
    print("@@ Predicting class......")
    pred, output_page = pred_plant_dieas(plant=file_path)
    print("File Path is : ",file_path)
               
    return render_template(output_page, pred_output = pred, user_image = 'user_upload'+'/'+filename)
     
# For local system &amp; cloud
if __name__ == "__main__":
  app.run(port="5001",debug=True)

