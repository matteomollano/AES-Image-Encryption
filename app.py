from flask import Flask, render_template, request, flash, redirect, url_for, send_file
from Encrypt import *
from Decrypt import *
import os
# from io import BytesIO
# from werkzeug.datastructures import FileStorage
# import tempfile

encryptionObj = Encrypt()
decryptionObj = Decrypt()
encryptedImagesList = []
decryptedImagesList = []

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.expanduser('~'), 'Downloads')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/encrypt")
def encrypt():
    global encryptedImagesList
    encryption_dict = encryptionObj.get_encryption_dict()
    for filename in encryption_dict:
        if filename not in encryptedImagesList:
            encryptedImagesList.append(filename)
    return render_template("encrypt.html", encrypted_files=encryptedImagesList)

@app.route('/process', methods=['POST'])
def process():
    global encryptionObj
    
    if request.method == 'POST':
        # save the password entered by the user
        text = request.form['encryption-key']
        # convert the password to a byte string
        password = bytes(text, 'utf-8')
        # set the object's key to the user entered password
        encryptionObj.set_key(password)
        iv = encryptionObj.get_iv()
        
        # print the key and iv
        print(f"The value entered in the textbox for encryption is {encryptionObj.get_key()}")
        print(f"The corresponding iv for encryption is {iv}")
        
    return redirect(url_for('encrypt'))
    
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    global encryptionObj, image_file
    if request.method == 'POST':
        # store the <FileStorage> object
        file = request.files['formFile']
        # get content of image (byte data)
        file_data = file.read()
        # store the filename
        filename = file.filename
        # perform encryption on image
        encryptionObj.encrypt_image(filename, file_data)
        
        # store password and initialization vector for that image
        password = encryptionObj.get_key()
        iv = encryptionObj.get_iv()
        encryptionObj.add_to_password_dict(password, iv)
        print(encryptionObj.get_password_dict())
        
    return redirect(url_for('encrypt'))
    
@app.route("/download", methods=['POST'])
def download():
    global encryptionObj, image, encrypted_file_name
    if request.method == 'POST':
        selected_item = request.form['selection-list']
        encryption_dict = encryptionObj.get_encryption_dict()
        
        for key, value in encryption_dict.items():
            if key == selected_item:
                image = value
                break
    
        # Generate a file path for the selected file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], selected_item)
        
        # save the encrypted image 
        with open(file_path, "wb") as f:
            f.write(image)
        
    return redirect(url_for('encrypt'))
                
@app.route("/decrypt")
def decrypt():
    global decryptedImagesList
    decryption_dict = decryptionObj.get_decryption_dict()
    for filename in decryption_dict:
        if filename not in decryptedImagesList:
            decryptedImagesList.append(filename)
    return render_template("decrypt.html", decrypted_files=decryptedImagesList)

@app.route("/process-decrypt", methods=['POST'])
def process_decrypt():
    global decryptionObj
    
    if request.method == 'POST':
        # save the password entered by the user
        text = request.form['decryption-key']
        # convert the password to a byte string
        password = bytes(text, 'utf-8')
        # set the object's key to the user entered password
        decryptionObj.set_key(password)
        
        # get the corresponding iv for this password
        password_dict = encryptionObj.get_password_dict()
        for key, iv in password_dict.items():
            if key == password:
                decryptionObj.set_iv(iv)
                break
            
        # store the iv
        iv = decryptionObj.get_iv()
        # print the key and iv
        print(f"The value entered in the textbox for decryption is {decryptionObj.get_key()}")
        print(f"The corresponding iv for decryption is {iv}")
        
    return redirect(url_for('decrypt'))

@app.route("/upload-decrypt", methods=['POST'])
def upload_decrypt():
    global decryptionObj, image_file
    if request.method == 'POST':
        # store the <FileStorage> object
        file = request.files['formFile']
        # get content of image (byte data)
        file_data = file.read()
        # store the filename
        filename = file.filename
        # perform encryption on image
        decryptionObj.decrypt_image(filename, file_data)
        
    return redirect(url_for('decrypt'))

@app.route("/download-decrypt", methods=['POST'])
def download_decrypt():
    global decryptionObj, image, decrypted_filename
    if request.method == 'POST':
        selected_item = request.form['selection-list']
        decryption_dict = decryptionObj.get_decryption_dict()
        
        for key, value in decryption_dict.items():
            if key == selected_item:
                image = value
                break  
            
        # Generate a file path for the selected file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], selected_item)
        
        # save the encrypted image 
        with open(file_path, "wb") as f:
            f.write(image)
        
    return redirect(url_for('decrypt'))
  
if __name__ == "__main__":
    app.run(debug=True)