from Crypto.Cipher import AES
import os

class Decrypt:
    
    def __init__(self) -> None:
        # decryption key (must be 16 bytes long)
        self.key = b''
        self.iv = b''
        # used to store key:value pairs of filename:actual decrypted file
        self.decryption_dict = {}
        
    def set_key(self, password):
        self.key = password
        
    def get_key(self):
        return self.key
    
    def set_iv(self, new_iv):
        self.iv = new_iv
    
    def get_iv(self):
        return self.iv
    
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
    
    def decrypt_image(self, filename, file):
        try: 
            # split up the encrypted filename --> puppy_encrypted.jpeg
            filename_list = self.split_filename(filename)
            # full_filename_list[0] = puppy_encrypted
            # full_filename_list[1] = jpeg
            name = filename_list[0]
            extension = filename_list[1]
            
            # split name into a list based on _ (underscore)
            name_split = self.split_name(name)
            new_name = name_split[0]
            
            # add _decrypted to the decrypted filename
            decrypted_filename = new_name + "_decrypted." + extension
            
            # create cipher object to perform encryption
            cipher = AES.new(self.key, AES.MODE_CFB, self.iv)
            
            # encrypt the original uploaded image
            decrypted_image = cipher.decrypt(file)
            
            # add the decrypted filename and the decrypted image byte content to the decryption_dict
            self.decryption_dict.update({decrypted_filename: decrypted_image})
            
            print("Successfully decrypted image")
            
        except:
            print("Decryption could not be handled")