#import seaborn as sns
#import matplotlib.pyplot as plt
import numpy as np
import pickle
import streamlit as st
#from sklearn.tree import plot_tree
from datetime import datetime
from PIL import Image

#loading saved model
loaded_model = pickle.load(open('C:/Users/Aniket/Desktop/model/trained_model.sav','rb'))

st.set_option('deprecation.showPyplotGlobalUse', False)
    
# giving the title
st.title("User Initiation Status - Let's Terra")


# Get the current time
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Display the current time using Streamlit
# Display the current time in bold and with a custom font using Markdown
st.markdown(f"<p style='font-family: Arial, sans-serif; font-weight: bold;'> Updated at : {current_time}</p>", unsafe_allow_html=True)

# Initiation Percentages
#lst = []

# Display an image from a local file
image_path = Image.open('C:/Users/Aniket/Desktop/img.png')
st.image(image_path,width=700,channels='RBG')

#m = loaded_model
#plt.figure(figsize=(30,15))  # Adjust the figure size as needed
#plot_tree(m, feature_names=["2finger_touch","dpad+camera","dpad_time","no_of_jumps","player_camera"], class_names=["0", "1",], filled=True,fontsize=20,max_depth=4)
#st.pyplot()
#creating a fuction for prediction

def prediction(input_data):
    
    #inp_data = [0,3,15,1,2]
    arr = np.asarray(input_data)
    arr = arr.reshape(1,-1)
    pred = loaded_model.predict(arr)

    if pred[0] == 0:
      out = 'Kid is not initiated'
    else:
      out = 'Kid is initiated'
      
    return out 


def men():
    
    # getting the input data 
    

    two_finger_touch = st.text_input('**Two finger touch count (0-200)**')
    dpad_camera = st.text_input('**Dpad + camera touch count (0-250)**')
    dpad_time = st.text_input('**Dpad touch time (0-200)**')
    no_of_jumps = st.text_input('**Number of jumps (0-200)**')
    #player_camera = st.text_input('**Camera touch count (0-10)**')
    
    option = st.selectbox(label="**Select Player Camera Count**",
                              options = ("0-50","50-100","100-150","150-200","200-250","250-300","300-350"))
                              
    if option == "0-50":
        player_camera=0
    elif option == "50-100":
        player_camera=1
    elif option == "100-150":
        player_camera=2
    elif option == "150-200":
        player_camera=3
    elif option == "200-250":
        player_camera=4
    elif option == "250-300":
        player_camera=5
    elif option == "300-350":
        player_camera=6
    
    
    
    #code for prediction
    op = ''
    
    #creating a button for prediction
    
    if st.button('**Predict Status**'):
        try:
            op = prediction([two_finger_touch,dpad_camera,dpad_time,no_of_jumps,player_camera])
            st.success(op)
            
        except :
            st.error("**Please enter valid input**")

    
if __name__ == '__main__':
    men()