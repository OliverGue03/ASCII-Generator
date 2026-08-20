from PIL import Image, ImageOps

# ASCII Character List, from "darkest" to "lightest" in color
ASCII_CHARACTERS = ["#", "@", "$", "§", "?", "&", "%", "*", ";", ":", ",", "."]

# Resizing the image with a width chosen by user
def resize_image(picture, new_width):
    width, height = picture.size
    ratio = width/height
    new_height = ratio * new_width
    return picture.resize(new_width, new_height)
            

def greyscale_image(picture):
    return ImageOps.grayscale(picture)

    
def generate_ascii(picture, size):
    img = Image.open(picture)
    resized_image = resize_image(img, size)
    grey_image = greyscale_image(resized_image)
    pixels = grey_image.getdata()

    ascii_pixels = ""
    for px in pixels:
        ascii_pixels.join(ASCII_CHARACTERS[px//25])

    return ascii_pixels


