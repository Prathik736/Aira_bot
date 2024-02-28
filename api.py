from authtoken import auth_token
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
import torch
from diffusers import StableDiffusionPipeline
from io import BytesIO
import base64

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

device = "cpu"
model_id = "C:/Users/scl/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, revision="fp32", torch_dtype=torch.float32, use_auth_token=auth_token)
pipe.to(device)

@app.get("/")
def generate(prompt: str):
    with torch.no_grad():
        image = pipe(prompt, guidance_scale=8.5).images[0]

    image.save("test_image.png")
    buffer = BytesIO()
    image.save(buffer, format='PNG')
    imgstr = base64.b64encode(buffer.getvalue())
    
    return Response(content=imgstr, media_type="image/png")

