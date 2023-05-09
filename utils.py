from PIL import Image
import io
from datetime import datetime 
import uuid 
from transformers import BlipProcessor, BlipForConditionalGeneration

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)


def image_to_text(image_bytes):
    raw_image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    inputs = processor(raw_image, return_tensors="pt")
    out = model.generate(**inputs)
    return processor.decode(out[0], skip_special_tokens=True)


def create_unique_uuid():
    return uuid.uuid4().hex


def get_timestamp():
    return datetime.now().isoformat()

def upload_to_blob(image_byte):

    bucket_name = "sidflasktest-347939299" 
    storage_client = storage.Client() 
    
    bucket = storage_client.bucket(bucket_name) 
    blob = bucket.blob(f"image_to_text/{create_unique_uuid()}")
    blob.upload_from_string(image_byte)
