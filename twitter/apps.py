from django.apps import AppConfig
from django.conf import settings
import os
import pickle

''''
import pickle
pickl = {
    'multinomialNB': multinomialNB,
    'countVectorizer': CountVectorizer,
    'clean_text': clean_text
}
pickle.dump( pickl, open( 'twitter' + ".sav", "wb" ) )
'''

class PredictorConfig(AppConfig):
    # create path to models
    path = os.path.join(settings.MODELS, 'twitter.sav')
 
    # load models into separate variables
    # these will be accessible via this class
    with open(path, 'rb') as pickled:
        data = pickle.load(pickled)
    multinomialNB = data['multinomialNB']
    countVectorizer = data['countVectorizer']
    # clean_text = data['clean_text']
