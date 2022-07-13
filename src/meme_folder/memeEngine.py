"""Construct meme."""
import os
import random
from PIL import Image, ImageFont, ImageDraw


class MemeEngine:
    """The engine behind meme generation."""

    def __init__(self, out_path):
        """Check if the directory already exists."""
        self.out_path = out_path

        if not os.path.isdir(self.out_path):
            os.mkdir(self.out_path)

    def generate_meme(self, img, quote_body, quote_author, width=400):
        """Construct meme."""
        outfile = os.path.join(self.out_path, f'{random.randint(0, 1000)}.jpg')
        image = Image.open(img)
        ratio = width / float(image.size[0])
        height = int(ratio * float(image.size[1]))
        new_image = image.resize((width, height), Image.NEAREST)

        draw = ImageDraw.Draw(new_image)
        message = quote_body + quote_author
        font = ImageFont.truetype("font/LilitaOne-Regular.ttf", size=20)
        draw.text((10, 30), message, font=font, fill='white')

        new_image.save(outfile, 'JPEG')
        return outfile
