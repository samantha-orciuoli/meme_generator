"""This is the DOCX ingestor."""
import docx
from .quote_model import QuoteModel
from .ingestor_interface import IngestorInterface


class DOCXIngestor(IngestorInterface):
    """Using the docx class."""

    viableFormats = ['docx']

    @classmethod
    def parse(cls, path: str):
        """Parse."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quote_models = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                new_quote = QuoteModel(parse[0], parse[1])
                quote_models.append(new_quote)

        return quote_models
