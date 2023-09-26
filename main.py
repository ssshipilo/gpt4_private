import os
from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
from flask_cors import CORS
from privateGPT import privateGPT

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['get'])
def home():
    return "GptOffline service point"

@app.route('/gpt', methods=['POST'])
def gpt_endpoint():
    """
    `Accepts Parameter`:\n
    { "text": "Your request"}\n
    To respond with a file\n
    {"file": "your file in blob/base64"}
    """
    try:
        input_text = request.form.get('text')
        if input_text is not None:
            type_req = "text"
            result = privateGPT(input_text, type_req)

            return result
        else:
            uploaded_file = request.get_data()
            filename = secure_filename(uploaded_file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            with open(filepath, 'wb') as file:
                file.write(uploaded_file)

            type_req = "file"
            result = privateGPT(filepath, type_req)
            os.remove(filepath)

            return str(result)
    except Exception as e:
        error_response = {
            'error': str(e)
        }
        return jsonify(error_response), 500

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(port=56663)