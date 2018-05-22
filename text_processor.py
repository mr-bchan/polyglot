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
        entities = {'I-ORG':[], 'I-PER':[], 'I-LOC':[]}

        print('Entities found in English language:')
        text = Text(blob, hint_language_code='en')
        print(text.entities)
        for e in text.entities:
            if e not in entities[e.tag]:
                print(e)
                entities[e.tag].append(' '.join(e))

        print('Entities found in Tagalog language:')
        text = Text(text, hint_language_code='tl')
        print(text.entities)
        for e in text.entities:
            if e not in entities[e.tag]:
                print(e)
                entities[e.tag].append(' '.join(e))

        print(entities)

    except Exception as e:
        print(e)
        entities = {'I-ORG':[], 'I-PER':[], 'I-LOC':[]}

    entities = {'entities': entities }

    return entities


def get_translated_text(blob):
    detector = Detector(blob)
    language = detector.language.code

    if language != 'en':
        text = Text(blob, hint_language_code='tl')
    else:
        text = Text(blob)

    return text