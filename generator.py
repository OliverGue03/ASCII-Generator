from PIL import Image

ASCII_CHARACTERS = ["#", "@", "$", "§", "?", "&", "%", "*", ",", ":"]

def resize_image(picture, new_width):
    width, height = picture.size
    ratio = width/height
    new_height = ratio * new_width
    return picture.resize(new_width, new_height)
            

def greyscale_image(picture):
    pass

def generate_ascii(picture, size):
    img = Image.open(picture)
    resize_image(img, size)
    greyscale_image(picture)
