# Image Caption Generator

This project is an **Image Caption Generator** web app built with **Streamlit** and powered by the **BLIP model** (BLIP-Image Captioning) from Hugging Face. It allows users to upload up to 3 images, which are processed to generate captions describing the contents of the images.

## Features

- Upload up to **3 images** at a time.
- Automatically generates captions for each image using a pre-trained model.
- Displays the images alongside their respective captions.
- Built with **Streamlit** for easy deployment.

## Requirements

- Python 3.7+
- Install the required Python packages:
  ```bash
  pip install streamlit transformers pillow

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/syfax-am/Image-Caption-Generator.git
2. Navigate into the project directory:
   ```bash
   cd Image-Caption-Generator
3. Run the Streamlit app:
  ```bash
  streamlit run app.py
  ```

## How It Works
1. The user uploads up to 3 images through the web interface.
2. The images are processed using the BLIP model from Hugging Face to generate captions.
3. The captions are displayed alongside the respective images in a clean, user-friendly layout.
   
## License
This project is licensed under the MIT License - see the LICENSE file for details.

### Future Improvements

* Add Multiple Caption Styles: Allow the user to select different captioning styles (e.g., humorous, detailed, concise).
* Image Processing Options: Provide options for resizing or adjusting images before captioning.
* Customizable Model: Integrate a feature where users can upload their own models or fine-tune the existing BLIP model for specific domains (e.g., fashion, nature).
* Batch Uploads: Support batch uploads of multiple images (more than 3) for users who want to generate captions for large sets of images.
* Language Support: Add multi-language support to generate captions in languages other than English.

