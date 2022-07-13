"""Create the format of quote on meme page."""


class QuoteModel:
    """Encapsulate quote."""

    def __init__(self, body: str, author: str):
        """Create a new QuoteModel."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Return body text - author."""
        return f'\"{self.body}\" - {self.author}'
        
    def __str__(self):
        """Return str(self)."""
        return self.body + " - " + self.author
