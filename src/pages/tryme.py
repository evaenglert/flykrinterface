import streamlit as st
import src.code.live_object_detection_asl as lod_asl

import src.code.app_flashcard_asl as fcard_asl

import src.code.app_flashcard_asl_fileupload as fcard_asl_upload

# pylint: disable=line-too-long
#Import for Deep learning model
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np

ASL = """
<div style="text-align: center" class="contributors font-body text-bold">
<a class="contributor comma" href="https://www.linkedin.com/in/franciska-e-94592115a/"><h4 style='text-align: center; color: black;'>Franciska Englert</h4</a>
</div>
"""


#deep learning sign detector model cached
@st.cache(allow_output_mutation=True)
def retrieve_model(PATH_MODEL, PATH_LABEL):
    """ dummy tensorflow CNN model trained on few epochs on multiclassification task (american signs) """
    # PATH_MODEL = "saved_models/asl_model2.h5"
    # PATH_LABEL = "saved_models/asl_class_names2.npy"

    model = tf.keras.models.load_model(PATH_MODEL)
    label = np.load(PATH_LABEL)
    return model, label

PATH_MODEL_ASL = "./saved_models/asl_model2.h5"
PATH_LABEL_ASL = "./saved_models/asl_class_names2.npy"

model_asl, label_asl = retrieve_model(PATH_MODEL_ASL, PATH_LABEL_ASL)

PATH_MODEL_ARABIC = "./saved_models/arabic_model.h5"
PATH_LABEL_ARABIC = "./saved_models/class_name_arabic.npy"



def write(mas=model_asl,
          lasl=label_asl,
          marab=model_arabic,
          larab=label_arabic):

    options = st.selectbox("Choose what you want to test today",
                           index=0,
                           options=[
                               "Live demo with American sign",

                               "Live Knowledge Test ASL w/ Flashcards",

                               "File upload Knowledge Test ASL w/ Flashcards"
                           ])

    if options=="Live demo with American sign":
        st.write("##")
        st.markdown(
            "<h4 style='text-align: center; color: black;'>Click on the start button to activate the webcam</h4",
                    unsafe_allow_html=True)
        st.write("##")
        lod_asl.app_object_detection_asl(model=mas, label=lasl)

    elif options=="Live Knowledge Test ASL w/ Flashcards":
        st.markdown(
            "<h4 style='text-align: center; color: black;'>Upload an image to test your knowledge about sign language</h4",
            unsafe_allow_html=True)
        st.write("##")
        fcard_asl.flashcard(model=mas, label=lasl)
        # # lod_arabic.app_object_detection_arabic()
        # flash_card = fcard.GameState()

    elif options == "File upload Knowledge Test ASL w/ Flashcards":
        st.markdown(
            "<h4 style='text-align: center; color: black;'>Upload an image to test your knowledge about sign language</h4",
            unsafe_allow_html=True)
        st.write("##")
        fcard_asl_upload.flashcard(model=mas, label=lasl)
