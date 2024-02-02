
import re
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet

class NLP():
    
    CONTRACTION_MAP = {
"ain't": "is not",
"aren't": "are not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he would",
"he'd've": "he would have",
"he'll": "he will",
"he'll've": "he he will have",
"he's": "he is",
"how'd": "how did",
"how'd'y": "how do you",
"how'll": "how will",
"how's": "how is",
"I'd": "I would",
"I'd've": "I would have",
"I'll": "I will",
"I'll've": "I will have",
"I'm": "I am",
"I've": "I have",
"i'd": "i would",
"i'd've": "i would have",
"i'll": "i will",
"i'll've": "i will have",
"i'm": "i am",
"i've": "i have",
"isn't": "is not",
"it'd": "it would",
"it'd've": "it would have",
"it'll": "it will",
"it'll've": "it will have",
"it's": "it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"mightn't've": "might not have",
"must've": "must have",
"mustn't": "must not",
"mustn't've": "must not have",
"needn't": "need not",
"needn't've": "need not have",
"o'clock": "of the clock",
"oughtn't": "ought not",
"oughtn't've": "ought not have",
"shan't": "shall not",
"sha'n't": "shall not",
"shan't've": "shall not have",
"she'd": "she would",
"she'd've": "she would have",
"she'll": "she will",
"she'll've": "she will have",
"she's": "she is",
"should've": "should have",
"shouldn't": "should not",
"shouldn't've": "should not have",
"so've": "so have",
"so's": "so as",
"that'd": "that would",
"that'd've": "that would have",
"that's": "that is",
"there'd": "there would",
"there'd've": "there would have",
"there's": "there is",
"they'd": "they would",
"they'd've": "they would have",
"they'll": "they will",
"they'll've": "they will have",
"they're": "they are",
"they've": "they have",
"to've": "to have",
"wasn't": "was not",
"we'd": "we would",
"we'd've": "we would have",
"we'll": "we will",
"we'll've": "we will have",
"we're": "we are",
"we've": "we have",
"weren't": "were not",
"what'll": "what will",
"what'll've": "what will have",
"what're": "what are",
"what's": "what is",
"what've": "what have",
"when's": "when is",
"when've": "when have",
"where'd": "where did",
"where's": "where is",
"where've": "where have",
"who'll": "who will",
"who'll've": "who will have",
"who's": "who is",
"who've": "who have",
"why's": "why is",
"why've": "why have",
"will've": "will have",
"won't": "will not",
"won't've": "will not have",
"would've": "would have",
"wouldn't": "would not",
"wouldn't've": "would not have",
"y'all": "you all",
"y'all'd": "you all would",
"y'all'd've": "you all would have",
"y'all're": "you all are",
"y'all've": "you all have",
"you'd": "you would",
"you'd've": "you would have",
"you'll": "you will",
"you'll've": "you will have",
"you're": "you are",
"you've": "you have"
}
    
    
    def quitar_simbolos(self, text, keep_apostrophes=False):
        '''
        '''
        sentence = sentence.strip() 
        if keep_apostrophes:
            PATTERN = r'[?|$|&|*|%|@|(|)|~]' # add other characters here to remove them
            filtered_sentence = re.sub(PATTERN, r'', sentence)
        else:
            PATTERN = r'[^a-zA-Z0-9 ]' # only extract alpha-numeric characters 
            filtered_sentence = re.sub(PATTERN, r'', sentence)
        return filtered_sentence
    
    def quitar_patron(self, text, patron):
        '''
        quitar patron usando libreria regex
        tipo '@[a-zA-Z0-9]'
        usar quitar_patron('@\w+',texto)
        '''
        return re.sub(patron, ' ', text)
    
    def quitar_espacios(self, text):
        '''
        '''
        return " ".join(text.split())    
    

    
    def expandir_contraccion(self, text): 
        '''
        '''
        contraction_mapping = self.CONTRACTION_MAP
        contractions_pattern = re.compile('({})'.format('|'.join(contraction_mapping.keys())),flags=re.IGNORECASE|re.DOTALL)
        def expand_match(contraction):
            match = contraction.group(0)
            first_char = match[0]
            expanded_contraction = contraction_mapping.get(match)\
                                    if contraction_mapping.get(match)\
                                    else contraction_mapping.get(match.lower()) 
            expanded_contraction = first_char+expanded_contraction[1:]
            return expanded_contraction
        
        expanded_text = contractions_pattern.sub(expand_match, text)
        expanded_text = re.sub("'", "", expanded_text)
        return expanded_text

    def tokenizar(self, text):
        '''
        '''
        tokens = nltk.word_tokenize(text)
        tokens = [token.strip() for token in tokens] 
        return tokens

#    def quitar_stopwords(self, text, exception=[], agregate=[]):
#        '''
#        '''
#        stopword_list = set(stopwords.words('english')) - set(exception) 
#        if len(agregate) > 0:
#            for i in range(0,len(agregate)):
#                stopword_list.add(agregate[i])
#        filtered_tokens = [token for token in text if token not in stopword_list]
#        return filtered_tokens

    def quitar_stopwords(self, text, exception=[], agregate=[]):
        '''
        defining the function to remove stopwords from tokenized text
        '''
        stop_words = set(stopwords.words('english')) - set(exception)
        if len(agregate) > 0:
            for i in range(0,len(agregate)):
                stop_words.add(agregate[i])
        output= " ".join([word for word in str(text).split() if word not in stop_words])
        #[i for i in text if i not in stopwords]
        return output 
    
    def quitar_palabras_repetidas(self, text): 
        '''
        '''
        repeat_pattern = re.compile(r'(\w*)(\w)\2(\w*)') 
        match_substitution = r'\1\2\3'
        def replace(old_word):
            if wordnet.synsets(old_word): 
                return old_word
            new_word = repeat_pattern.sub(match_substitution, old_word) 
            return replace(new_word) if new_word != old_word else new_word

        correct_tokens = [replace(word) for word in text] 
        return correct_tokens


class NLP_es():


    def reemplazar_sp(self,text):
        '''
        '''
        a,b = 'áéíóúüñ','aeiouun'
        trans = str.maketrans(a,b)
        return text.translate(trans)


    def quitar_stopwords(self, text, exception=[], agregate=[]):
        '''
        defining the function to remove stopwords from tokenized text
        '''
        stop_words = set(stopwords.words('spanish')) - set(exception)
        if len(agregate) > 0:
            for i in range(0,len(agregate)):
                stop_words.add(agregate[i])
        output= " ".join([word for word in str(text).split() if word not in stop_words])
        #[i for i in text if i not in stopwords]
        return output 
    
    def quitar_espacios(self, text):
        '''
        '''
        return " ".join(text.split())  
    
    def quitar_simbolos(self, text, keep_apostrophes=False):
        '''
        '''
        sentence = sentence.strip() 
        if keep_apostrophes:
            PATTERN = r'[?|$|&|*|%|@|(|)|~]' # add other characters here to remove them
            filtered_sentence = re.sub(PATTERN, r'', sentence)
        else:
            PATTERN = r'[^a-zA-Z0-9 ]' # only extract alpha-numeric characters 
            filtered_sentence = re.sub(PATTERN, r'', sentence)
        return filtered_sentence
    
    def quitar_patron(self, text, patron):
        '''
        quitar patron usando libreria regex
        tipo '@[a-zA-Z0-9]'
        usar quitar_patron('@\w+',texto)
        '''
        return re.sub(patron, ' ', text)