from flask import Flask, Response, request
from flask_cors import CORS
import torch
from diffusers import StableDiffusionPipeline
from io import BytesIO
import base64


app = Flask(__name__)
CORS(app)

device = "cpu"
model_id = "C:/Users/scl/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, revision="fp32", torch_dtype=torch.float32)
pipe.safety_checker = lambda images, clip_input: (images,False) # to stop the deteecting NSFW
pipe.enable_attention_slicing()
pipe.to(device)

@app.route('/', methods=['GET'])
def generate():
    prompt = request.args.get('prompt')
    with torch.no_grad():
        image = pipe(prompt, guidance_scale=8.5).images[0]

    image.save("test_image.png")
    buffer = BytesIO()
    image.save(buffer, format='PNG')
    imgstr = base64.b64encode(buffer.getvalue())
    
    return Response(imgstr, mimetype="image/png")

if __name__ == '__main__':
    app.run(debug=True)
