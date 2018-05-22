from polyglot.detect import Detector
from polyglot.text import Text

def get_sentiment(blob):
    try:
        text = get_translated_text(blob)
        polarity = text.polarity
    except Exception:
        polarity = 0

    sentiment = {'polarity': polarity }

    return sentiment


def get_entities(blob):
    try:
        entities = {}

        text = Text(blob, hint_language_code='en')

        print('Entities found:')
        print(text.entities)
        
        for e in text.entities:
            entities[e.tag].append(' '.join(e))

    except Exception:
        entities = {'I-ORG':[], 'I-PER':[], 'I-LOC':[]}

    entities = {'entities': entities }

    return entities


def get_translated_text(blob):
    detector = Detector(blob)
    language = detector.language.code

    if language is not 'en':
        text = Text(blob, hint_language_code='tl')
    else:
        text = Text(blob)

    return text