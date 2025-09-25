import streamlit as st
import base64
import random
import os


def get_image_data(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def img_path_creator(color):
    base_path = (
        r"C:\Users\Dell\Desktop\Python_Streamlit_PR.-3-Navratri-Dandiya\assets\imgs"
    )
    return os.path.join(base_path, f"dandiya_{color}.png")


st.title("Let's Play Dandiya!")

colors = ["red", "blue", "green", "yellow", "purple", "orange"]

# STEP 1: User picks color first (always visible)
picked_color = st.selectbox(
    "Pick a stick color", options=["-- Select a color --"] + colors
)

# STEP 2: Then they click Play button
if st.button("Play Dandiya"):
    if picked_color == "-- Select a color --":
        st.warning("Please select a color to play Dandiya!")
    else:
        st.balloons()
        token = random.randint(100000, 999999)

        # image data
        dandiya_image = get_image_data(img_path_creator(picked_color))

        html_code = f"""
        <div style="display:flex; flex-direction:column; align-items:center; gap:12px; margin-top:20px;">
          <div style="display:flex; justify-content:center; gap:50px;">
            <img src="data:image/png;base64,{dandiya_image}" class="d1_{token}" style="width:100px;">
            <img src="data:image/png;base64,{dandiya_image}" class="d2_{token}" style="width:100px;">
          </div>

          <div style="margin-top:8px; display:flex; gap:10px; align-items:center;">
            <div style="width:36px; height:36px; border-radius:6px; border:1px solid #ccc; background:{picked_color};"></div>
            <div style="font-weight:600;">Selected stick color: {picked_color.capitalize()}</div>
          </div>
        </div>

        <style>
        @keyframes rotate1_{token} {{
          from {{ transform: rotate(45deg); }}
          to   {{ transform: rotate(-45deg); }}
        }}
        @keyframes rotate2_{token} {{
          from {{ transform: rotate(-45deg); }}
          to   {{ transform: rotate(45deg); }}
        }}
        .d1_{token} {{
          animation: rotate1_{token} 0.7s ease-in-out;
          animation-fill-mode: both;
        }}
        .d2_{token} {{
          animation: rotate2_{token} 0.7s ease-in-out;
          animation-fill-mode: both;
        }}
        </style>
        """
        st.markdown(html_code, unsafe_allow_html=True)

st.markdown("---")
st.info(
    "Thank you!\nFeel free to explore more about it and happy coding!🚀\n- ***Prath-Digital*** 🧑🏻‍💻"
)
