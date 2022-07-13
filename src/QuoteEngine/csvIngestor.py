"""This is the CSV Ingestor."""

import pandas as pd
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class CSVIngestor(IngestorInterface):
    """Using the csv class."""

    viableFormats = ['csv']

    @classmethod
    def parse(cls, path: str):
        """Parse."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quote_models = []
        df = pd.read_csv(path, header=0)

        for index, row in df.iterrows():
            print()
            new_quote = QuoteModel(row['body'], row['author'])
            quote_models.append(new_quote)

        return quote_models
