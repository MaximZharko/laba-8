from PIL import Image


with Image.open("picture.jpeg") as img:
    img.load()
    new_img = img.crop((0, 0, 400, 800))
    new_img.save("new_picture.jpeg")

