"""PDF ingestor."""
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
import os
import random
import subprocess


class PDFIngestor(IngestorInterface):
    """For pdf files."""

    viableFormats = ['pdf']

    @classmethod
    def parse(cls, path: str):
        """Parse."""
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        file = os.path.join(f'static/{random.randint(0, 100000)}.txt')
        with open(file, 'w'):
            cmd = f"./pdftotext -layout -nopgbrk {path} {file}"
            subprocess.call(['pdftotext', path, file])

        quote_models = []
        new_file = open(file, 'r')
        for line in new_file.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                items = line.split('-')
                new_quote = QuoteModel(items[0], items[1])
                quote_models.append(new_quote)

        new_file.close()
        os.remove(file)
        return quote_models
