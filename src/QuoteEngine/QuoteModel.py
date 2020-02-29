class QuoteModel():

    def __init__(self, body: str, author: str):

        """Create a new QuoteModel"""
        self.body = body
        self.author = author

    def __repr__(self):
        """ return ”body text” - author """
        return f'\"{self.body}\" - {self.author}'
