from Crypto.Cipher import AES
import os

class Encrypt:
    
    def __init__(self) -> None:
        # encryption key (must be 16 bytes long)
        self.key = b''
        # iv = initialization vector
        # the initialization vector is used to ensure that encrypting the same image multiple
        # times will not result in the exact same cipher text
        self.iv = os.urandom(16)
        # used to store key:value pairs of filename:actual encrypted file
        self.encryption_dict = {}
        # used to store key:value pairs of password:initialization vector (IV)
        self.password_dict = {}
    
    def set_key(self, password):
        self.key = password
        
    def get_key(self):
        return self.key
    
    def get_iv(self):
        return self.iv
    
    def add_to_password_dict(self, password, iv):
        self.password_dict.update({password:iv})
        
    def get_password_dict(self):
        return self.password_dict
    
    def add_to_encryption_dict(self, filename, file):
        self.encryption_dict.update({filename:file})
        
    def get_encryption_dict(self):
        return self.encryption_dict
    
    def add_to_decryption_dict(self, filename, file):
        self.decryption_dict.update({filename:file})
    
    def get_decryption_dict(self):
        return self.decryption_dict
    
    def split_filename(self, filename):
        file_list = filename.split(".")
        return file_list
    
    def split_name(self, name):
        name_list = name.split("_")
        return name_list
    
    def encrypt_image(self, filename, file):
        try: 
            # split the filename into an array of name and extension
            # for example, puppy.jpeg = ['puppy', 'jpeg']
            filename_list = self.split_filename(filename)
            name = filename_list[0]
            extension = filename_list[1]
            
            # add _encrypted to the original filename
            encrypted_filename = name + "_encrypted." + extension
            
            # create cipher object to perform encryption
            cipher = AES.new(self.key, AES.MODE_CFB, self.iv)
            
            # encrypt the original uploaded image
            encrypted_image = cipher.encrypt(file)
            
            # add the encrypted filename and the encrypted image byte content to the encryption_dict
            self.encryption_dict.update({encrypted_filename: encrypted_image})
            
            print("Successfully encrypted image")
            
        except:
            print("Encryption could not be handled")