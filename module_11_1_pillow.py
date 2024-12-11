import os, sys
from PIL import Image

size = (1720, 920)

im = Image.open("Метода поиска заказов.jpg")


for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)[0] + ".thumbnail"
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.thumbnail(size)
                im.save(outfile, 'JPEG')
        except OSError:
            print("cannot create thumbnail convert", infile)

for infile in sys.argv[1:]:
    try:
        with Image.open(infile) as im:
            print(infile, im.format, f"{im.size}x{im.mode}")
    except OSError:
        ...

box = (0, 0, 64, 64)
region = im.crop(box)

region = region.transpose(Image.Transpose.ROTATE_180)
im.paste(region, box)
print(im.format, im.size, im.mode)

def roll(im: Image.Image, delta: int) -> Image.Image:
    xsize, ysize = im.size

    delta = delta % xsize
    if delta == 0:
        return im

    part1 = im.crop((0, 0, delta, ysize))
    part2 = im.crop((delta, 0, xsize, ysize))
    im.paste(part1, (xsize - delta, 0, xsize, ysize))
    im.paste(part2, (0, 0, xsize - delta, ysize))

    return im

show = roll(im, 500)
print(show)

def merge(im1: Image.Image, im2: Image.Image) -> Image.Image:
    w = im1.size[0] + im2.size[0]
    h = max(im1.size[1], im2.size[1])
    im = Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))

    return im
im.show()