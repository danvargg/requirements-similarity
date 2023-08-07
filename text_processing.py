"""Text processing functionalities."""


class TextProcessor:
    """Text processing functionalities."""

    def __init__(self, text):
        """Initialize the text processor."""
        self.text = text

    def remove_punctuation(self):
        """Remove punctuation from the text."""
        self.text = self.text.replace('.', '')
        self.text = self.text.replace(',', '')
        self.text = self.text.replace(';', '')
        self.text = self.text.replace(':', '')
        self.text = self.text.replace('!', '')
        self.text = self.text.replace('?', '')
        self.text = self.text.replace('(', '')
        self.text = self.text.replace(')', '')
        self.text = self.text.replace('[', '')
        self.text = self.text.replace(']', '')
        self.text = self.text.replace('{', '')
        self.text = self.text.replace('}', '')
        self.text = self.text.replace('"', '')
        self.text = self.text.replace("'", '')
        self.text = self.text.replace('`', '')
        self.text = self.text.replace('´', '')
        self.text = self.text.replace('’', '')
        self.text = self.text.replace('‘', '')
        self.text = self.text.replace('“', '')
        self.text = self.text.replace('”', '')
        self.text = self.text.replace('…', '')
        self.text = self.text.replace('–', '')
        self.text = self.text.replace('-', '')
        self.text = self.text.replace('_', '')
        self.text = self.text.replace('—', '')
        self.text = self.text.replace('/', '')
        self.text = self.text.replace('\\', '')
        self.text = self.text.replace('|', '')
        self.text = self.text.replace('«', '')
        self.text = self.text.replace('»', '')
        self.text = self.text.replace('°', '')
        self.text = self.text.replace('º', '')
