import streamlit as st
import random


# ===============================
# Function to get the raw GitHub image URL
# ===============================
def get_image_url(color):
    base_url = "https://raw.githubusercontent.com/Prath-Digital/Python_Streamlit_PR.-3-Navratri-Dandiya/main/assets/imgs"
    return f"{base_url}/dandiya_{color}.png"


# ===============================
# App Title
# ===============================
st.title("Hi Guys, Let's Play Dandiya!")

# ===============================
# Available colors
# ===============================
colors = ["red", "blue", "green", "yellow", "purple", "orange"]

# STEP 1: User picks a color
picked_color = st.selectbox(
    "Pick a stick color", options=["== Select a color =="] + colors
)

# STEP 2: Play button
if st.button("Play Dandiya"):
    if picked_color == "== Select a color ==":
        st.warning("Please select a color to play Dandiya!\nThe colors are in the dropdown above.")
    else:
        st.balloons()
        token = random.randint(100000, 999999)

        # Get image URL
        image_url = get_image_url(picked_color)

        # Animated sticks using HTML/CSS
        html_code = f"""
        <div style="display:flex; flex-direction:column; align-items:center; gap:12px; margin-top:20px;">
          <div style="display:flex; justify-content:center; gap:50px;">
            <img src="{image_url}" class="d1_{token}" style="width:100px;">
            <img src="{image_url}" class="d2_{token}" style="width:100px;">
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

# ===============================
# Footer
# ===============================
st.markdown("===")
st.info(
    "Thank you!\nFeel free to explore more about it and happy coding! 🚀\n- ***Prath-Digital*** 🧑🏻‍💻"
)
