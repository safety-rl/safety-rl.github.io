from PIL import Image, ImageDraw, ImageFont
from matplotlib import font_manager


from os import listdir
from os.path import isfile, join
folder = "static/images/locomotion"
files = [ f for f in listdir(folder) if f.endswith(".png") ]

font_file = 'scripts/Courier_New.ttf'

nrows = 3
ncols = 4

imsize = 300

new_im = Image.new('RGB', (imsize*ncols,(imsize+40)*nrows), (255,255,255))

index = 0
for i in range(0,imsize*nrows,imsize+40):
    for j in range(0,imsize*ncols,imsize):
        im = Image.open(join(folder, files[index]))
        im.thumbnail((imsize,imsize))
        im_with_caption = Image.new('RGB', (imsize,imsize+40), (255,255,255))
        im_with_caption.paste(im, (0,0))
        d = ImageDraw.Draw(im_with_caption)
        d.fontmode = "L"
        fnt = ImageFont.truetype(font_file, 20)
        caption = files[index].split("-")[1]
        caption = caption.split("_")[0]
        # d.text((imsize/2,imsize), caption, font=fnt, fill=(1,0,0))
        _, _, w, h = d.textbbox((0, 0), caption, font=fnt)
        d.text((imsize/2-w/2,imsize), caption, font=fnt, fill=(1,0,0))
        print("file: ", caption)
        new_im.paste(im_with_caption, (j,i))
        index += 1
        if index == len(files) and index < nrows*ncols:
            block_width = imsize*(ncols - 1)
            block_height = (imsize+40)
            block = new_im.crop((0, i, block_width, i+block_height))
            new_im.paste((255,255,255), (0, i, block_width, i+block_height))
            new_im.paste(block, (imsize//2, i))
            break

new_im.save(folder+".png")