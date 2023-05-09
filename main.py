from flask import Flask , request, jsonify 
from datetime import datetime 
from utils import image_to_text 

app = Flask(__name__)


@app.route("/", methods = ['GET','POST']) 
def index(): 
    if request.method == "POST": 
        file = request.files.get('file')
        if file is None or file.filename == "": 
            return jsonify({'error':'no file'})

        try: 
            print(f"\n\n\n\n{request.remote_addr}\n\n\n\n")
            image_bytes = file.read() 
            data = image_to_text(image_bytes)
            return jsonify({'prediction':data})   
        except Exception as e: 
            return jsonify({'error': str(e)})
    return "Welcome"

if __name__ == "__main__": 
    app.run(debug = True)
