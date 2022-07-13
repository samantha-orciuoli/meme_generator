"""This is an ingestor guide."""
from .ingestor_interface import IngestorInterface
from .csvIngestor import CSVIngestor
from .txtIngestor import TXTIngestor
from .docxIngestor import DOCXIngestor
from .pdfIngestor import PDFIngestor


class Ingestor(IngestorInterface):
    """This is to see if we can ingest the file."""

    ingestors = [CSVIngestor, DOCXIngestor, TXTIngestor, PDFIngestor]
    
    @classmethod
    def parse(cls, path: str):
        """Parse."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
