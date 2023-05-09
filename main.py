from flask import Flask , request, jsonify 
from datetime import datetime 
from utils import image_to_text , upload_to_blob 

app = Flask(__name__)


@app.route("/", methods = ['GET','POST']) 
def index(): 
    if request.method == "POST": 
        file = request.files.get('file')
        if file is None or file.filename == "": 
            return jsonify({'error':'no file'})

        try: 
            image_bytes = file.read() 
            upload_message = upload_to_blob(image_bytes)
            data = image_to_text(image_bytes)
            return jsonify({'prediction':data,'upload_message': upload_message})   
        except Exception as e: 
            return jsonify({'error': str(e)})
    return "Welcome"

if __name__ == "__main__": 
    app.run(debug = True)
