import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Set the page title
st.set_page_config(page_title="Image Caption Generator", page_icon="📸")

# Load the BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Streamlit interface
st.title("Image Caption Generator")
st.write("Upload up to 3 images to generate captions.")

# Image uploader (allow multiple images, but limit to 3)
uploaded_images = st.file_uploader("Choose up to 3 images...", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

# Check if the number of uploaded images exceeds 3
if uploaded_images and len(uploaded_images) > 3:
    st.error("Please upload a maximum of 3 images.")
    uploaded_images = uploaded_images[:3]  # Keep only the first 3 images

if uploaded_images:
    # Define columns for displaying images in 3 columns
    num_images = len(uploaded_images)
    cols = st.columns(3)  # Create 3 columns for layout
    
    # Iterate over the images and display each one with its caption
    for idx, uploaded_image in enumerate(uploaded_images):
        # Open and process the image
        image = Image.open(uploaded_image).convert("RGB")

        # Select column to display image and caption
        col = cols[idx % 3]  # Cycle through columns
        
        # Display the image in the current column with width of 200px
        with col:
            st.image(image, caption=f"Uploaded Image {idx + 1}", use_container_width=False, width=200)

            # Prepare input for the model
            inputs = processor(images=image, return_tensors="pt")

            # Generate the caption
            out = model.generate(**inputs, max_new_tokens=50)
            caption = processor.decode(out[0], skip_special_tokens=True)

            # Display the generated caption for the image
            st.write(f"**Caption**: {caption}")
