import streamlit as st
import numpy as np
import pickle

# Load the fitted model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit App Setup
st.title("🔍 Rock vs Mine Classifier")

st.markdown("Paste exactly **60 comma-separated feature values** (from sonar signals):")

# Input Field
input_values = st.text_area("Example: 0.03, 0.04, ..., 0.0199", "")

if st.button("Predict"):
    try:
        # Clean and parse input
        sanitized = input_values.replace('\n', '').strip()
        value_list = [float(x.strip()) for x in sanitized.split(',') if x.strip()]

        if len(value_list) != 60:
            st.error(f"❌ You entered {len(value_list)} values. Exactly 60 required.")
        else:
            input_array = np.array(value_list).reshape(1, -1)
            prediction = model.predict(input_array)
            label = "🪨 Rock" if prediction[0] == 'R' else "💣 Mine"
            st.success(f"Prediction: **{label}**")

    except Exception as e:
        st.error("⚠️ Error processing input. Make sure all values are numeric and properly formatted.")
        st.exception(e)