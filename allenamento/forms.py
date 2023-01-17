from django import forms
from .models import Schedario,Blocco
from django.contrib.auth.models import User


# create a workout
class CreaSchedaModelForm(forms.ModelForm):

    class Meta:
        model=Schedario
        fields=["nome_scheda"]
        exclude=["user","numero_mipiace","pubblica","tirata","spinta","addominali","gambe","pull","push","abs","legs"]


#create a workout block
class CreaBloccoModelForm(forms.ModelForm):

    class Meta:
        model=Blocco
        fields=["esercizio","set","reps","zavorra","duration"]
        exclude=["nome_scheda"]
        labels={
            "zavorra"  : "zavorra (Kg)",
            "duration" : " durata in secondi",
        }
    def __init__(self, *args, **kwargs):
        super(CreaBloccoModelForm, self).__init__(*args, **kwargs)
        self.fields['set'].required = False
        self.fields['reps'].required = False
        self.fields['zavorra'].required = False
        self.fields['duration'].required = False   



# create an USER
class FormRegistrazioneUser(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput())
    email=forms.CharField(widget=forms.EmailInput())
    password=forms.CharField(widget=forms.PasswordInput())
    conferma_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=["username","email","password","conferma_password"]
        

    def clean(self):
        super().clean()
        password=self.cleaned_data["password"]
        conferma_password=self.cleaned_data["conferma_password"]
        if password != conferma_password:
            raise forms.ValidationError("le password non combaciano")
        return self.cleaned_data    

