from PIL import Image
import numpy as np
import requests
from io import BytesIO

def download_image(url):
    # Download the image from the URL
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

def encrypt_image(image_url, key):
    # Download the image from URL
    img = download_image(image_url)
    width, height = img.size
    
    # Convert image to numpy array for fast pixel access
    img_array = np.array(img)
    
    # Encrypt each pixel value
    encrypted_img_array = img_array ^ key
    
    # Convert back to image from numpy array
    encrypted_img = Image.fromarray(encrypted_img_array)
    
    # Save encrypted image
    encrypted_image_path = 'encrypted_image.png'  # or use a filename of your choice
    encrypted_img.save(encrypted_image_path)
    
    print(f"Image encrypted successfully and saved as {encrypted_image_path}")
    return encrypted_image_path

def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_image_path)
    
    # Convert image to numpy array for fast pixel access
    encrypted_img_array = np.array(encrypted_img)
    
    # Decrypt each pixel value
    decrypted_img_array = encrypted_img_array ^ key
    
    # Convert back to image from numpy array
    decrypted_img = Image.fromarray(decrypted_img_array)
    
    # Save decrypted image
    decrypted_image_path = 'decrypted_image.png'  # or use a filename of your choice
    decrypted_img.save(decrypted_image_path)
    
    print(f"Image decrypted successfully and saved as {decrypted_image_path}")
    return decrypted_image_path

# Example usage
image_url = 'https://filmfare.wwmindia.com/content/2021/apr/ramcharan21617713712.jpg'
key = 123  # Example key, you can choose any integer as your key

# Encrypt the image
encrypted_image_path = encrypt_image(image_url, key)

# Decrypt the image
decrypted_image_path = decrypt_image(encrypted_image_path, key)
