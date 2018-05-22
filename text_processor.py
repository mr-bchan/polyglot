from polyglot.detect import Detector
from polyglot.text import Text

def get_sentiment(blob):

    detector = Detector(blob)
    language = detector.language.code

    if language is not 'en':
        text = Text(blob, hint_language_code='tl')
    else:
        text = Text(blob)

    try:
        polarity = text.polarity
    except Exception:
        polarity = 0

    sentiment = {'polarity': polarity }

    return sentiment