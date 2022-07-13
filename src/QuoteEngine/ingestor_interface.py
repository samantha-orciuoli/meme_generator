"""This checks what the program can ingest and what it cannot."""
from abc import ABC, abstractmethod


class IngestorInterface(ABC):
    """Check to see if we can ingest."""

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Check file format."""
        for viableFormat in cls.viableFormats:
            if viableFormat in path:
                return True
            else:
                return False
    
    @classmethod
    @abstractmethod
    def parse(cls, path: str):
        """Pass."""
        pass
