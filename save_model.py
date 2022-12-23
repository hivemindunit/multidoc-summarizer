import sys
import nltk

def save_model():
    """Download nltk data."""
    nltk.download('punkt', download_dir='./nltk_data')

if __name__ == "__main__":
    save_model()