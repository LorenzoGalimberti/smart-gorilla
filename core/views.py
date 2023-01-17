from django.shortcuts import render,redirect
from allenamento.models import Esercizio,Schedario,Blocco,Muscoli
from core.models import MiPiace
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from django.db.models import Q

# Create your views here.

# homepage
def home(request):
    esercizi=Esercizio.objects.all()
    context={'esercizi':esercizi}
    return render(request,'homepage.html',context)

# research an exercise 
def cerca(request):
    if "q" in request.GET:
        querystring=request.GET.get("q")
        if len(querystring) == 0:
            return redirect("/cerca/")
        esercizi=Esercizio.objects.filter(Q(nome__icontains=querystring)|Q(tipo__tipo__icontains=querystring))
        muscoli=Muscoli.objects.all()
        #esercizi_tipo=Esercizio.objects.filter(tipo__tipo__icontains=querystring)
        context={"esercizi":esercizi,'muscoli': muscoli}
        return render(request,"esercizi_page.html",context)
    else:
        esercizi=Esercizio.objects.all().order_by("nome")
        muscoli=Muscoli.objects.all()
        context={"esercizi":esercizi,'muscoli': muscoli}
        return render(request,"esercizi_page.html",context)



# i like it
def mi_piace(request,slug):
    scheda=Schedario.objects.get(slug=slug)
    mi_piace=MiPiace.objects.filter(scheda=scheda)
    mi_piace_list=[]
    for like in mi_piace:
        mi_piace_list.append(like.user)
    if request.user.is_authenticated and request.user not in mi_piace_list:
        user= MiPiace.objects.create(
            scheda=scheda,
            user=request.user,
        )   
        scheda.numero_mipiace=scheda.numero_mipiace +1
        scheda.save(update_fields=['numero_mipiace'])
        mi_piace=MiPiace.objects.filter(scheda=scheda)

        blocchi=Blocco.objects.filter(nome_scheda=scheda)
        return HttpResponseRedirect(f"/schedario/{scheda.slug}")

    if request.user.is_authenticated and request.user  in mi_piace_list:
        
        scheda.numero_mipiace=scheda.numero_mipiace -1
        scheda.save(update_fields=['numero_mipiace']) 
        user=MiPiace.objects.get(scheda=scheda,user=request.user)
        user.delete()
        mi_piace=MiPiace.objects.filter(scheda=scheda)

        blocchi=Blocco.objects.filter(nome_scheda=scheda)
        return HttpResponseRedirect(f"/schedario/{scheda.slug}")
         
      

    # schedario=Schedario.objects.all()
    # mi_piace=MiPiace.objects.filter(scheda=scheda)

    # blocchi=Blocco.objects.filter(nome_scheda=scheda)
    # context={'scheda':scheda ,'blocchi':blocchi,'mi_piace':mi_piace}
    # #return HttpResponseRedirect(f"/schedario/{scheda.pk}")
    
    # return render(request,'scheda.html',context)
    
 

#_---- PUBBLICA -------------

def pubblica(request,slug):
    scheda=Schedario.objects.get(slug=slug)
    scheda.pubblica=True
    scheda.save()
    return HttpResponseRedirect(f"/schedario/{scheda.slug}")




