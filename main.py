# main.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from authtoken import auth_token
from diffusers import StableDiffusionPipeline
from io import BytesIO
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import base64
import torch

app = FastAPI()
auth_token = "Aira_bot"
# Configure FastAPI to serve static files from the "static" directory
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

templates = Jinja2Templates(directory="templates")

device = "cpu"
model_id = "C:/Users/scl/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, revision="fp32", torch_dtype=torch.float32, use_auth_token=auth_token)
pipe.to(device)

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate_image/")
async def generate_image(prompt: str = Form(...)):
    with torch.no_grad():
        image = pipe(prompt, guidance_scale=8.5).images[0]

    buffer = BytesIO()
    image.save(buffer, format='PNG')
    imgstr = base64.b64encode(buffer.getvalue())
    
    return {"image_data": imgstr.decode('utf-8')}
