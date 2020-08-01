from PIL import Image
from PIL import ImageFilter
im = Image.open('lemon.png')

im.show()

print(im.format, im.size, im.mode)
size = (128, 128)
im.thumbnail(size)
im.show()
im.save('thumbnail.jpg', 'JPEG')

rotated = im.rotate(45)
rotated.save('rotated.jpg', 'JPEG')
rotated.show()

transposed = im.transpose(Image.FLIP_TOP_BOTTOM)
transposed.show()

detail = im.filter(ImageFilter.DETAIL)
detail.show()

greyscale = im.convert('L')
greyscale.show()
