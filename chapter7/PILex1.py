from PIL import Image
im = Image.open("school.jpg")
print(im.format,im.size,im.mode)
