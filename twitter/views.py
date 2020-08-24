from .apps import PredictorConfig
from django.http import JsonResponse
from rest_framework.views import APIView

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer 
from string import punctuation as pun
import re
from django.shortcuts import render

sw, stem=[x for x in stopwords.words('english') if x not in ['not', 'no', 'nor']], PorterStemmer()
def clean_text(text, stop_words=sw, stemer=stem):
    return " ".join([stemer.stem(w.lower()) for w in word_tokenize(re.sub(f'[{pun}]', '', text)) if w not in stop_words])

class analysis_tweet(APIView):
    def get(self, request):
        x_text = PredictorConfig.countVectorizer.transform([clean_text(request.GET.get('tweet_text'))])
        prediction = PredictorConfig.multinomialNB.predict(x_text)[0]
        prob = PredictorConfig.multinomialNB.predict_proba(x_text)
        return JsonResponse({'class':f'{prediction}', 'predict_proba':f'{prob}'})


def my_view(request):
    # View code here...
    return render(request, 'twitter/index.html')