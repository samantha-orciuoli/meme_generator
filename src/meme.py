"""This file is to construct the meme."""
import os
import random
import argparse

from meme_folder.memeEngine import MemeEngine
from QuoteEngine.ingestor import Ingestor
from QuoteEngine.quote_model import QuoteModel


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given path and quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.generate_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a meme.")
    parser.add_argument('--system_path', type=str,
                        default='/Users/Chris/Desktop/src/')
    parser.add_argument('--path', type=str, default=None)
    parser.add_argument('--body', type=str, default=None)
    parser.add_argument('--author', type=str, default=None)

    args = parser.parse_args()
    system_path = args.system_path
    path = args.path
    body = args.body
    author = args.author
    print(generate_meme(args.path, args.body, args.author))
