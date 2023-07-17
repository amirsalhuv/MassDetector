import streamlit as st
#from rembg import remove
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(layout="wide", page_title="Breast lesion detector")

st.write("## Assistive tool for automatic inspection of lesion in a breast image")
st.write(
    "This Tool enables you the option to detect, segement and analyse a breast mammography X-ray image "
)
st.sidebar.write("## Upload new image :gear:")


# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload):
    image = Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)

    #fixed = remove(image)
    col2.write("Fixed Image :wrench:")
    #col2.image(fixed)
    st.sidebar.markdown("\n")
    #st.sidebar.download_button("Download fixed image", convert_image(fixed), "fixed.png", "image/png")


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    fix_image(upload=my_upload)
else:
    fix_image("./zebra.jpg")
