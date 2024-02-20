import spacy
# from spacy.tokens import Doc

# NER = Named Entity Recognition
# This class is used to recognize stations (also lines and direction) in a text message


class TransportInformationRecognizer:
    def __init__(self, model_path='NER/models/loss17'):
        self.model_path = model_path
        
        self.nlp = spacy.load(f'{self.model_path}')
        self.ner = self.nlp.get_pipe('ner')

        print(f'model {self.model_path} loaded')

    # input: text message (string)
    # return: a list of all recognized stations in the text
    def get_recognized_stations(self, text: str) -> list:
        
        match = self.nlp(text)
        matches = []
        for entity in match.ents:
            if entity.label_ == 'STATION':
                matches.append(entity)
            
        return matches

    # input: text message (string)
    # return: a text message with only the recognized stations
    def process_text(self, text: str) -> list:

        doc = self.nlp(text)
        stations = []

        for entity in doc.ents:
            if entity.label_ == 'STATION':
                stations.append(entity.text)

        return stations
    

TextProcessor = TransportInformationRecognizer('NER/models/loss17')
