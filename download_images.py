import requests
import os

# URL of the GitHub repository containing the images
base_url = "https://github.com/Code-Institute-Solutions/boutique_ado_images"

# List of image filenames to download
image_filenames = [
    "image1.jpg",
    "image2.jpg",
    # Add more filenames as needed
]

# Directory to save the downloaded images
media_dir = os.path.join(os.path.dirname(__file__), 'media', 'images')

# Create the directory if it doesn't exist
os.makedirs(media_dir, exist_ok=True)

# Function to download an image
def download_image(filename):
    url = base_url + filename
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(os.path.join(media_dir, filename), 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {filename}: {e}")

# Download all images
for filename in image_filenames:
    download_image(filename)
