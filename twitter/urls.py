from django.urls import path
from . import views
urlpatterns = [
    path('api/', views.analysis_tweet.as_view()),
    path('', views.my_view),
]