from django.db import models
from allenamento.models import Schedario
from django.contrib.auth.models import User
# Create your models here.
# like system model
class MiPiace(models.Model):
    scheda=models.ForeignKey(Schedario,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

# discussion model
class Discussione(models.Model):

    """  singola discussione specifica di una 
         scheda . accessibile a tutti gli utenti"""

    titolo=models.CharField(max_length=120)
    data_creazione=models.DateTimeField(auto_now_add=True)
    autore_descrizione= models.ForeignKey(User,on_delete=models.CASCADE,related_name='discussione')
    scheda_appartenenza=models.ForeignKey(Schedario,on_delete=models.CASCADE)

    def __str__(self):
        return self.titolo

    class Meta:
        verbose_name="Discussione"
        verbose_name_plural="Discussioni"