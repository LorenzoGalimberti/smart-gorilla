from django.urls import path
from .views import timer,esercizio_view,crea_allenamento,registrazione,scheda_view,schedario_view,crea_blocco,elimina_blocco,le_mie_schede

urlpatterns = [
   path('esercizi/<slug:slug>/',esercizio_view,name='esercizio-view'),
   path('crea-allenamento/',crea_allenamento,name='crea-allenamento'), 
   path('registrati/',registrazione,name='registration'),
   path('schedario/',schedario_view,name='schedario-view'),
   path('schedario/<slug:slug>/',scheda_view,name='scheda-view'),
   path('le-mie-schede/',le_mie_schede,name='mie-schede-view'),
   path('schedario/<slug:slug>/crea-blocco/',crea_blocco,name='crea-blocco'),
   path('schedario/<slug:slug>/elimina-blocco/<int:id>/',elimina_blocco,name='elimina-blocco'),
   path('schedario/<slug:slug>/<int:id>/timer',timer,name='timer-blocco'),
  
]
