from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from diffusers import StableDiffusionPipeline
from fastapi.staticfiles import StaticFiles
from io import BytesIO
import base64
import torch

app = FastAPI()

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
pipe = StableDiffusionPipeline.from_pretrained(model_id, revision="fp32", torch_dtype=torch.float32)
pipe.to(device)

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate_image/")
async def generate_image(prompt: str = Form(...)):
    with torch.no_grad():
        images = pipe(prompt, guidance_scale=8.5).images

    image_data = []
    for image in images[:4]:
        buffer = BytesIO()
        image.save(buffer, format='PNG')
        imgstr = base64.b64encode(buffer.getvalue()).decode('utf-8')
        image_data.append({"image_data": imgstr})

    return image_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
