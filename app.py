from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/encrypt")
def encrypt():
    return render_template("encrypt.html")

@app.route("/decrypt")
def decrypt():
    return render_template("decrypt.html")
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      file = request.files['file']
      return 'file uploaded successfully'