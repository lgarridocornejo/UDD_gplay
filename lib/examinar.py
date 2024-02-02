#20231121
#20240202

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

import random
import string
string.punctuation
import re

import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from unicodedata import normalize

class EDA():

    def __init__(self,df, color=None):
        '''
        '''
        self.df = df
        self.columnas = df.columns
        self.color = color
    
    def hexcolor(self, qty):
        random.seed(10)
        color = []
        for i in range(0,qty):
            color.append('#' + '%06x' % random.randint(0, 0xFFFFFF))
        return color    

    def duplicados(self,col):
        '''
        xxx.duplicados(['col1','col2',..'coln'])
        '''
        print(f'***** El dataset original contiene {self.df.shape[0]} registros y {self.df.shape[1]} atributos')
        
        dfdup = self.df.duplicated(subset=col)
        print(f'Total de registros unicos: \033[1m{self.df[~dfdup].shape[0]}\033[0m')

        if self.df[dfdup].shape[0]==0:
            print('No se registran duplicados')

        if self.df[dfdup].shape[0]>0:
            print(f'Total de registros duplicados: \033[1m{self.df[dfdup].shape[0]}\033[0m')
            self.df = self.df[~dfdup]
            print(f'***** El dataset sin duplicados contiene {self.df.shape[0]} registros y {self.df.shape[1]} atributos\n')
            return self.df
        
    def infoplus(self):
        '''
        Despliegue de la informacion acerca del set de datos, conteniendo:
        Nombre y tipo de la columna.
        Cantidad de registros y faltantes, asi como su porcentaje.
        Unico, cantidad de atributos de la columna
        '''
        registro = []
        colmax80 = []
        colmin80 = []
        for col in list(self.columnas):
            var = []
            var.append(col)
            var.append(str(self.df[col].dtypes))
            var.append(self.df[col].count())
            var.append(self.df.shape[0]-self.df[col].count())
            var.append(round((1 - ((self.df.shape[0]-self.df[col].count()) / self.df.shape[0])) * 100,4))
            var.append(len(self.df[col].unique()))
            registro.append(var)
        dftotal = pd.DataFrame(registro, columns=['columna','tipo','total','faltantes','pct','unico'])
        dftotal = dftotal.sort_values(by = 'pct', ascending = False)

        if (self.df.count().sum()/self.df.size)*100 != 100:
            print(f'El porcentaje de completitud es de: \033[1m{(self.df.count().sum()/self.df.size)*100:.1f}\033[0m%\n')

        return dftotal 
    
    def histograma(self,columnas):
        '''
        '''
        cm = plt.colormaps.get_cmap(self.color)
        
        data = self.df[columnas]
        bin = 'sturges'
        if len(data.shape) < 2:
            qty = 1
        else:
            qty = data.shape[1]
        fig, ax = plt.subplots(1, qty,figsize=(qty*5,4))    
        #columnas = col)
        for i in range(0, qty):
            titulo = 'Histograma: ' + columnas[i]

            if qty==1:
                ax.set_title(titulo)
                n, bins, patches = ax.hist(self.df[columnas[i]],bins=bin)  
                col = (n-n.min())/(n.max()-n.min())
                for c, p in zip(col, patches):
                    plt.setp(p, 'facecolor', cm(c)) 
            else:
                n, bins, patches = ax[i].hist(self.df[columnas[i]],bins=bin,facecolor='purple')
                ax[i].set_title(titulo)
                col = (n-n.min())/(n.max()-n.min())
                for c, p in zip(col, patches):
                    plt.setp(p, 'facecolor', cm(c)) 

        plt.tight_layout()  
        plt.show() 
        
        
    def labeler(self,pct, allvals):
        absolute = pct/100.*np.sum(allvals)
        return "{:.1f}%\n({:.0f})".format(pct, absolute)
        #autopct=lambda p: '{:.2f}%({:.0f})'.format(p,(p/100)*days.sum()))


        
    def dona(self,columnas,etiqueta={}):
        '''
        '''
        COLORS = gcolor = ['#ea4235','#34a855','#4385f6','#f9bb04','#9a9c08']#['#0e5893','#db6100','#1b8011','#b40c0d','#74499c','#6d392e','#c157a0','#616161','#9a9c08']
        tipo = type(columnas)
        if tipo == dict:
            col = columnas
            col_filter = columnas['col_filter']
            col_target = columnas['col_target']
            columnas = list(self.df[col_filter].unique())

        qty = len(columnas) 

        fig, ax = plt.subplots(1, qty,figsize=(qty*5,5))

        for i in range(0, qty):
            if tipo == dict:

                unique, counts = np.unique(self.df[self.df[col_filter]==columnas[i]][col_target], return_counts=True)
                total = sum(counts)
                #print(unique,counts,total)
            else:
                unique, counts = np.unique(self.df[columnas[i]], return_counts=True) 
                total = sum(counts)
                #print(unique,counts,total)

            if len(etiqueta)!= 0:
                unique = [etiqueta.get(n, n) for n in unique]
            titulo = 'Relación atributos variable: ' + columnas[i]
            #print(unique,counts,titulo)

            if qty==1:
                ax.set_title(titulo)
                wedges, texts, autotexts = ax.pie(counts,
                                           autopct=lambda pct: self.labeler(pct, counts),
                                           radius=1,
                                           colors = COLORS,
                                           startangle=90,
                                           textprops=dict(color="w"),
                                           wedgeprops=dict(width=0.7, edgecolor='w'))

                ax.legend(wedges, unique,
                           loc=4,#'center right',
                           bbox_to_anchor=(0.7, 0, 0.5, 1))

                plt.text(0,0, 'TOTAL\n{}'.format(total),
                            weight='bold', size=12, color='#52527a',
                             ha='center', va='center')

                plt.setp(autotexts, size=12, weight='bold')
                ax.axis('equal')  # Equal aspect ratio
#                plt.savefig(columnas[i],bbox_inches='tight')


            else:
                ax[i].set_title(titulo)
                wedges, texts, autotexts = ax[i].pie(counts,
                                           autopct=lambda pct: self.labeler(pct, counts),
                                           radius=1,
                                           colors = COLORS,   
                                           startangle=90,
                                           textprops=dict(color="w"),
                                           wedgeprops=dict(width=0.7, edgecolor='w'))

                ax[i].legend(wedges, unique,
                           loc=4, #'center right',
                           bbox_to_anchor=(0.7, 0, 0.5, 1))

                ax[i].text(0,0, 'TOTAL\n{}'.format(total),
                            weight='bold', size=12, color='#52527a',
                             ha='center', va='center')

                plt.setp(autotexts, size=12, weight='bold')
                ax[i].axis('equal')  # Equal aspect ratio
                #ax[i].savefig(columna[i])
    
        plt.savefig('img/'+columnas[i],bbox_inches='tight')
        plt.tight_layout() 
        plt.show()         
     
    
      
class nlang():

    def quitar_simbolos(self, text):
        '''
        defining the function to remove punctuation
        '''
        simbolos = "".join([i for i in text if i not in string.punctuation])
        return simbolos  
    
    def tokenizar(self, text):
        '''
        defining function for tokenization
        '''
        tokens = word_tokenize(text)
        #tokens = re.split('W+',text)
        return tokens    

    def quitar_stopwords(self, text, argumento = []):
        '''
        defining the function to remove stopwords from tokenized text
        '''
        stop_words = set(stopwords.words('english'))
        if len(argumento) > 0:
            for i in range(0,len(argumento)):
                stop_words.add(argumento[i])
        output= " ".join([word for word in str(text).split() if word not in stop_words])
        #[i for i in text if i not in stopwords]
        return output     
    
    def quitar_patron(self, text, patron):
        '''
        quitar patron usando libreria regex
        tipo '@[a-zA-Z0-9]'
        usar quitar_patron('@\w+',texto)
        '''
        return re.sub(patron, ' ', text)
    
    def reemplazar_sp(self,text):
        '''
        '''
        a,b = 'áéíóúüñ','aeiouun'
        trans = str.maketrans(a,b)
        return text.translate(trans)

    def quitar_espacios(self, text):
        return " ".join(text.split())   
    
    def quitar_html(self, text):
        '''
        takes a string `text` as the input
        returns a string without HTML tags
        '''
        pattern = re.compile('<.*?>')
        output = pattern.sub(r'', text)
        return output
    
    def quitar_refuser(self, text):
        '''
        quita las referencia a los usuarios
        tipo @nombre_usuario
        '''
        pattern = re.compile('@\w+')
        output = pattern.sub(r'', text)
        return output        
           
    def quitar_url(self, text):
        '''
        takes a string `text` as the input
        returns a string without any URL
        '''
        pattern = re.compile(r'https?://\S+|www\.\S+')
        output = pattern.sub(r'', text)
        return output    
        
    def stemming(self, text):
        '''
        defining a function for stemming
        '''
        porter_stemmer = PorterStemmer()
        stem_text = [porter_stemmer.stem(word) for word in text]
        return stem_text    
    
    def lematizar(self, text, encoding="utf8"):
        '''
        defining the function for lemmatization
        '''
        #wordnet_lemmatizer = WordNetLemmatizer()
        #lemm_text = [wordnet_lemmatizer.lemmatize(word) for word in text]
        #return lemm_text
    
#def words_lemmatizer(text, encoding="utf8"):
        words = nltk.word_tokenize(text) 
        lemma_words = []
        wl = WordNetLemmatizer()
        for word in words:
            pos = self.find_pos(word)
            lemma_words.append(wl.lemmatize(word, pos).encode(encoding)) 
        return " ".join(lemma_words)

    def find_pos(self, word):
        # Part of Speech constants
        # ADJ, ADJ_SAT, ADV, NOUN, VERB = 'a', 's', 'r', 'n', 'v'
        # You can learn more about these at http://wordnet.princeton.edu/ wordnet/man/wndb.5WN.html#sect3
        # You can learn more about all the penn tree tags at https://www.ling. upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
        pos = nltk.pos_tag(nltk.word_tokenize(word))[0][1]
        # Adjective tags - 'JJ', 'JJR', 'JJS'
        if pos.lower()[0] == 'j':
            return 'a'
        # Adverb tags - 'RB', 'RBR', 'RBS' 
        elif pos.lower()[0] == 'r':
            return 'r'
        # Verb tags - 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ' 
        elif pos.lower()[0] == 'v':
            return 'v'    
    
    
    def expandir_contraccion(self, text):
        contraction_dict = {"ain't": "are not","'s":" is","aren't": "are not", "i'm":"i am"}
        contractions_re=re.compile('(%s)' % '|'.join(contractions_dict.keys()))
        def replace(match):
            return contractions_dict[match.group(0)]
        return contractions_re.sub(replace, text)
    


    
    
  