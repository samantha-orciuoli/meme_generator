"""TXT ingestor."""

from .quote_model import QuoteModel
from .ingestor_interface import IngestorInterface


class TXTIngestor(IngestorInterface):
    """Creating a class for importing txt files."""

    viableFormats = ['txt']

    @classmethod
    def parse(cls, path: str):
        """Parse."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quote_models = []
        document = open(path, 'r')

        for line in document:
            items = line.split('-')
            new_quote = QuoteModel(items[0], items[1])
            print(new_quote)
            quote_models.append(new_quote)

        return quote_models
