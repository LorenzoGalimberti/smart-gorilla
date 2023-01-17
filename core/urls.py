from django.urls import path
from .views import home,cerca,mi_piace,pubblica

urlpatterns = [
   path('',home,name='homeview'),
   path('esercizi/',cerca,name='funzione_cerca'),
   path('schedario/<slug:slug>/mi-piace',mi_piace,name='mi-piace'),
   path('schedario/<slug:slug>/condividi',pubblica,name='condividi'),
  

]
