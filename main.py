import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# --- Page Configuration ---
st.set_page_config(
    page_title="🌿 Plant Disease Detection",
    page_icon="🌱",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- Helper Function for Prediction ---
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_plant_disease_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions)

# --- Sidebar ---
st.sidebar.title("🌾 Plant Disease Detection")
st.sidebar.markdown("### 🧠 AI-Powered Crop Health Analysis")
app_mode = st.sidebar.radio("📍 Select Page", ["🏠 Home", "🧬 Disease Recognition", "👨‍💻 About"])

# --- Home Page ---
if app_mode == "🏠 Home":
    st.markdown(
        """
        <h1 style='text-align: center; color: #2E8B57;'>🌿 Plant Disease Detection</h1>
        <h3 style='text-align: center; color: #4CAF50;'>for Sustainable Agriculture 🌱</h3>
        """,
        unsafe_allow_html=True
    )
    st.image("Diseases.png", use_container_width=True, caption="Healthy vs Diseased Leaves")

    st.markdown(
        """
        <div style="text-align: center; font-size: 18px;">
            🌻 Upload a plant leaf image to identify if it’s healthy or infected.<br>
            🌾 Empowering farmers with AI technology for a greener future!
        </div>
        """,
        unsafe_allow_html=True
    )

# --- Prediction Page ---
elif app_mode == "🧬 Disease Recognition":
    st.markdown(
        "<h2 style='color: #2E8B57; text-align:center;'>🔍 Plant Disease Detection</h2>",
        unsafe_allow_html=True
    )

    test_image = st.file_uploader("📤 Choose an Image", type=["jpg", "jpeg", "png"])

    if test_image:
        st.image(test_image, use_container_width=True, caption="Uploaded Image 🌿")

        if st.button("🚀 Predict"):
            with st.spinner("Analyzing the image... please wait ⏳"):
                result_index = model_prediction(test_image)

            class_name = [
                'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew',
                'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
                'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy',
                'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
                'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy',
                'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
                'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew',
                'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot',
                'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold',
                'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite',
                'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                'Tomato___healthy'
            ]

            st.success(f"🌱 The model predicts this is **{class_name[result_index]}** 🍃")

# --- About Page ---
elif app_mode == "👨‍💻 About":
    st.markdown(
        """
        <h2 style='color: #2E8B57;'>👩‍🌾 About This Project</h2>
        <p style='font-size: 18px;'>
        This Streamlit app uses a deep learning model trained on the PlantVillage dataset 🌾 
        to detect plant leaf diseases. It supports multiple crops like <b>Tomato, Apple, Corn, Potato</b>, and more! 🍅🍎🌽🥔
        </p>
        <hr>
        """,
        unsafe_allow_html=True
    )

# --- Footer (always visible) ---
st.markdown(
    """
    <hr>
    <div style='text-align: center; padding-top: 10px; color: gray; font-size: 16px;'>
        🌿 Made with ❤️ by <b>Gurudeep Soni</b> | © 2025 Plant Disease Detection
    </div>
    """,
    unsafe_allow_html=True
)
