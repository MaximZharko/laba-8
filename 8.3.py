from PIL import Image, ImageDraw, ImageFont


print("Введи имя своего друга:")
name = input()
with Image.open("picture.jpeg") as img:
    img.load()
    new_img = img
    draw = ImageDraw.Draw(new_img)
    my_font = ImageFont.truetype("myfont.ttf", size=100)
    draw.text((20, new_img.height // 2),
              name + " ,поздравляю!",
              font=my_font,
              fill=("white"))
    new_img.save("new_picture.png")
