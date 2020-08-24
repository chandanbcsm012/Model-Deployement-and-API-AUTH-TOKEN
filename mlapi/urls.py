from django.urls import path, include
urlpatterns = [
    path('classify/', include('predictor.urls')),
    path('twitter/',  include('twitter.urls')),
    path('core/',  include('core.urls'))
]
