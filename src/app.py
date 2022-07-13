"""Run this file for final project."""
import random
import os
import requests
from flask import Flask, render_template, request

from meme_folder.memeEngine import MemeEngine
from QuoteEngine.ingestor import Ingestor

app = Flask(__name__)


def setup():
    """Refer to the dog quotes to grab."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        try:
            quotes.extend(Ingestor.parse(f))
        except ValueError as error:
            print(f"ValueError: {error}")

    images_path = "./_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]
    return quotes, imgs


meme = MemeEngine('./static')
quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.generate_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    img = "./temp_image.jpg"
    image_url = request.form.get("image_url")
    img_data = requests.get(image_url, stream=True).content
    try:
        with open(img, "wb") as f:
            f.write(img_data)

        body = request.form.get("body", "")
        author = request.form.get("author", "")
        path = meme.generate_meme(img, body, author)
        print(path)
        os.remove(img)
        return render_template("meme.html", path=path)
    finally:
        return render_template("error.html")


if __name__ == "__main__":
    app.run()
