from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import random
import os
import os.path


def edit_img(text):
    phraseTop = 'С днем'
    phraseBottom = text

    img = Image.open(f'assets/{get_random_img()}')
    width, height = img.size
    I1 = ImageDraw.Draw(img)

    fontsize = 1
    img_fraction = 0.70
    font = ImageFont.truetype(
        'Fonts/TOYZ.ttf', size=fontsize, encoding='UTF-8')
    while font.getsize(phraseBottom)[0] < img_fraction*img.size[0]:
        fontsize += 1
        font = ImageFont.truetype(
            'Fonts/TOYZ.ttf', size=fontsize, encoding='UTF-8')
    fontsize -= 1
    font = ImageFont.truetype(
        'Fonts/TOYZ.ttf', size=fontsize, encoding='UTF-8')

    wTop, hTop = I1.textsize(phraseTop, font=font)
    wBottom, hBottom = I1.textsize(phraseBottom, font=font)

    I1.text(((width-wTop)/2, (height-hTop)/15), phraseTop, font=font,
            stroke_width=2, stroke_fill='black', fill='#6B3074')
    I1.text(((width-wBottom)/2, (height-hBottom)/1.1), phraseBottom,
            font=font, stroke_width=2, stroke_fill='black', fill='#6B3074')

    return img


def get_random_img():
    files_list = os.listdir('./assets')
    return files_list[random.randint(0, len(files_list)-1)]


if __name__ == '__main__':
    edit_img('ебейшего похмелья').show()
