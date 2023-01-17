from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
from django.core.validators import MaxValueValidator, MinValueValidator

# Tipo di esercizio
class Tipi(models.Model):
    tipo=models.CharField(max_length=15)

    def __str__(self):
        return self.tipo



# EXERCISE MODEL
class Esercizio(models.Model):
    nome=models.CharField(max_length=20)
    slug=models.SlugField()
    tipo=models.ForeignKey(Tipi,on_delete=models.CASCADE)
    time=models.BooleanField()
    url=EmbedVideoField()
    #aggiungere in futuro immagini e vidoe
    def __str__(self):
        return self.nome
#MUSCLE MODEL
class Muscoli(models.Model):
    muscolo= models.CharField(max_length=20)
    #esercizio_correlato=models.ForeignKey(Esercizio,on_delete=models.CASCADE)
    esercizio=models.ManyToManyField(Esercizio)
    def __str__(self):
        return self.muscolo

# WORKOUT PLAN MODEL
class Schedario(models.Model):
    nome_scheda=models.CharField(max_length=20,unique=True)
    slug=models.SlugField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    numero_mipiace=models.IntegerField(default=0)
    pubblica=models.BooleanField(default=False)
    tirata = models.IntegerField(default=0)
    spinta = models.IntegerField(default=0)
    addominali = models.IntegerField(default=0)
    gambe = models.IntegerField(default=0)
    pull = models.IntegerField(default=0)
    push = models.IntegerField(default=0)
    abs = models.IntegerField(default=0)
    legs = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nome_scheda
# EORKOUT CHUNK --> each w.o plan is composed in blocks of exercises
class Blocco(models.Model):
    esercizio=models.ForeignKey(Esercizio,on_delete=models.CASCADE)
    nome_scheda=models.ForeignKey(Schedario,on_delete=models.CASCADE)
    set=models.IntegerField(blank=True,null=True)
    reps=models.IntegerField(blank=True,null=True)
    zavorra=models.IntegerField(blank=True,null=True)
    duration=models.IntegerField(default=0,blank=True,null=True)
    def __str__(self):
        return self.esercizio.nome

    
    