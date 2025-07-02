This repository contains an implementation of a web-based image generation service using [Stable Diffusion](https://huggingface.co/CompVis/stable-diffusion). 
Users can generate AI-generated images by providing a textual prompt, and the app will return generated images using the Stable Diffusion model.

## Features

- Generate images from text prompts using the Stable Diffusion model.
- Web-based interface built with [FastAPI](https://fastapi.tiangolo.com/) and [Flask](https://flask.palletsprojects.com/).
- Image results displayed in the browser and served as base64-encoded PNGs.
- Includes CORS middleware to allow cross-origin requests.

## Requirements
- CPU : i7 13700k or Higher
- GPU : NVIDIA RTX 3060 Or Higher
- RAM : 16GB or Higher
- Python 3.8+
- [PyTorch](https://pytorch.org/) (CPU or GPU)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Flask](https://flask.palletsprojects.com/)
- [Hugging Face Diffusers](https://huggingface.co/docs/diffusers/index)

## Setup Instructions

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/stable-diffusion-image-generator.git
   cd stable-diffusion-image-generator
   ```
Install the required Python packages:
```
pip install -r requirements.txt
Download and set up the Stable Diffusion model. You can use the pretrained model from Hugging Face:
```
```
from diffusers import StableDiffusionPipeline
import torch
```
```
model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
```
Run the FastAPI server:
```
uvicorn main:app --reload
Access the application in your browser at http://127.0.0.1:8000.
```

Usage
Navigate to the root URL (/) and enter a text prompt to generate an image.

The image will be generated and displayed on the web page, or available as base64-encoded PNG data.

Flask Server Alternative
An alternative Flask implementation is included for serving the image generation via a Flask API.

Run the Flask server:
```
python flask_app.py
Access the Flask API at http://127.0.0.1:5000/?prompt=YOUR_PROMPT to generate an image from the provided prompt.
```
Example
Here's a basic example of how the app can be used:
```
curl -X POST "http://127.0.0.1:8000/generate_image/" -F "prompt='A futuristic cityscape with neon lights'"
#The generated image will be returned as base64-encoded PNG data.
```
Contributing
Feel free to submit pull requests and issues. Contributions are always welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributors
Prathik
Guna Asher

### Steps to Update
1. Update the repository URL, model details, and other relevant information.
2. Customize contributor details or add additional sections such as "Troubleshooting" or "Advanced Configuration" if needed.





