# Code Depot Presents: Image Downloader and Displayer
# This Python script downloads images from given URLs and displays them using OpenCV
# For more exciting projects, visit https://www.patreon.com/CodeDepot

# Import the necessary packages
import numpy as np
import urllib.request
import cv2


# Function to download image from URL and convert it to OpenCV format
def url_to_image(url):
    print(f"[Code Depot] Accessing URL: {url}")

    # Download the image from the URL
    resp = urllib.request.urlopen(url)

    # Convert the downloaded image to a NumPy array
    image = np.asarray(bytearray(resp.read()), dtype="uint8")

    # Decode the NumPy array into OpenCV format
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    print("[Code Depot] Image successfully converted to OpenCV format.")

    # Return the image
    return image


# Initialize the list of image URLs to download
print("[Code Depot] Initializing list of image URLs.")
urls = [
    "https://images.unsplash.com/photo-1692970095410-6bd548fc7f6c?auto=format&fit=crop&q=80&w=2428&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1693306051445-ef70b0deb6cb?auto=format&fit=crop&q=80&w=2187&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1692297351816-9fa5d0483608?auto=format&fit=crop&q=80&w=2187&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
]

# Loop over the image URLs
counter = 1
for url in urls:
    print(f"[Code Depot] Downloading image {counter} from the list.")

    # Download the image from the URL and display it
    image = url_to_image(url)

    # Generate filename and save the image in the current directory
    filename = f"image_{counter}.jpg"
    cv2.imwrite(filename, image)
    print(f"[Code Depot] Image saved as {filename}")

    counter += 1

    # Display the image
    print("[Code Depot] Displaying the image.")
    cv2.imshow("Image", image)
    cv2.waitKey(0)

print("[Code Depot] All images have been successfully downloaded and displayed.")