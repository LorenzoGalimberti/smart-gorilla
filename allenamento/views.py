from django.shortcuts import render
from core.models import MiPiace
from .models import Esercizio,Schedario,Blocco,Muscoli
from .forms import CreaSchedaModelForm,FormRegistrazioneUser,CreaBloccoModelForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.utils.text import slugify

# Create your views here.
def esercizio_view(request,slug):
    esercizio=Esercizio.objects.get(slug=slug)
    muscoli=Muscoli.objects.filter(esercizio=esercizio)
    
    context={'esercizio':esercizio,'muscoli': muscoli}
    return render(request,'esercizio_page.html',context)

# def esercizi_view(request):
#     esercizi=Esercizio.objects.all().order_by("nome")
#     muscoli=Muscoli.objects.all()
#     context={'esercizi':esercizi,'muscoli': muscoli}
#     return render(request,'esercizi_page.html',context)

def crea_allenamento(request):
    if request.method == 'POST':
        form=CreaSchedaModelForm(request.POST)
        if form.is_valid():
            print('form valido')
            form.instance.slug=slugify(form.instance.nome_scheda)
            form.instance.user=request.user
            nuova_scheda=form.save()
            print(nuova_scheda.pk)
            print('nome scheda : ',form.cleaned_data["nome_scheda"])
            return HttpResponseRedirect(f"/schedario/{nuova_scheda.slug}") # mettere un REDIRECT alla view della scheda 
    
    else:
        form=CreaSchedaModelForm()
    context={'form':form}    
    
    return render(request,'crea_allenamento.html',context)


def registrazione(request):
    if request.method == 'POST':
        form=FormRegistrazioneUser(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            User.objects.create_user(
                username=username,
                password=password,
                email=email
            )            
            user=authenticate(username=username,password=password)
            login(request,user)
            return HttpResponseRedirect("/")
    else:
        form=FormRegistrazioneUser()
    context={"form":form}

    return render(request,"registrazione.html",context)        




# view della scheda

def scheda_view(request,slug):
    scheda=Schedario.objects.get(slug=slug)
    blocchi=Blocco.objects.filter(nome_scheda=scheda)
    mi_piace=MiPiace.objects.filter(scheda=scheda)
    mi_piace_list=[]
    for like in mi_piace:
        mi_piace_list.append(like.user)
    context={'scheda':scheda,"blocchi":blocchi,"mi_piace":mi_piace_list}
    return render(request,'scheda.html',context)


def schedario_view(request):
    esercizi=Esercizio.objects.all()
    schedario=Schedario.objects.filter(pubblica=True).order_by('-numero_mipiace')
    context={'schedario':schedario,"esercizi":esercizi}
    for scheda in schedario:
        print(scheda)
    return render(request,'schedario.html',context)

def le_mie_schede(request):
    schede=Schedario.objects.filter(user=request.user)
    context={'schede':schede}
    return render(request,'mie_schede.html',context)

# CRUD BLOCKS

def crea_blocco(request,slug):
    scheda=Schedario.objects.get(slug=slug)
    print(scheda.user)
    if scheda.user == request.user: #abilitato ad aggiungere
        if request.method == 'POST':
            form=CreaBloccoModelForm(request.POST)
            if form.is_valid():
                esercizio=form.cleaned_data["esercizio"]
                nome_scheda=scheda
                set=form.cleaned_data["set"]
                reps=form.cleaned_data["reps"]
                zavorra=form.cleaned_data["zavorra"]
                esercizio=Esercizio.objects.get(nome=esercizio)
                duration=form.cleaned_data["duration"]
                #block=Blocco(esercizio=esercizio,nome_scheda=nome_scheda,set=set,reps=reps,comment=comment)
                Blocco.objects.create(
                    esercizio=esercizio,
                    nome_scheda=nome_scheda,
                    set=set,
                    reps=reps,
                    zavorra=zavorra,
                    duration=duration,
                )            
                if str(esercizio.tipo)=='tirata':
                    scheda.tirata+=1
                    scheda.pull=(scheda.tirata*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
                    scheda.push=(scheda.spinta*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
                    scheda.abs=(scheda.addominali*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
                    scheda.legs=(scheda.gambe*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
                    scheda.save()

                if str(esercizio.tipo)=='spinta':
                    scheda.spinta+=1
                    scheda.pull=(scheda.tirata*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
                    scheda.push=(scheda.spinta*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
                    scheda.abs=(scheda.addominali*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
                    scheda.legs=(scheda.gambe*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
                    scheda.save()

                if str(esercizio.tipo)=='addominali':
                    scheda.addominali+=1
                    scheda.pull=(scheda.tirata*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
                    scheda.push=(scheda.spinta*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
                    scheda.abs=(scheda.addominali*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
                    scheda.legs=(scheda.gambe*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
                    scheda.save()
                if str(esercizio.tipo)=='gambe':
                    scheda.gambe +=1
                    scheda.pull=(scheda.tirata*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
                    scheda.push=(scheda.spinta*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
                    scheda.abs=(scheda.addominali*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
                    scheda.legs=(scheda.gambe*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
                    scheda.save()
                
                # modifico i valori di tirata,spinta,addominali,gambe
                return HttpResponseRedirect(f"/schedario/{scheda.slug}")
        else:
            form=CreaBloccoModelForm()
    context={"scheda":scheda,"form":form}
    return render(request,"crea_blocco.html",context)


def elimina_blocco(request,slug,id):
    
    scheda=Schedario.objects.get(slug=slug)
    blocco=Blocco.objects.get(id=id)
    if str(blocco.esercizio.tipo)=='tirata':
        scheda.tirata-=1
        scheda.pull=(scheda.tirata*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
        scheda.push=(scheda.spinta*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
        scheda.abs=(scheda.addominali*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
        scheda.legs=(scheda.gambe*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
        scheda.save()

    if str(blocco.esercizio.tipo)=='spinta':
        scheda.spinta-=1
        scheda.pull=(scheda.tirata*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
        scheda.push=(scheda.spinta*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
        scheda.abs=(scheda.addominali*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
        scheda.legs=(scheda.gambe*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
        scheda.save()

    if str(blocco.esercizio.tipo)=='addominali':
        scheda.addominali-=1
        scheda.pull=(scheda.tirata*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
        scheda.push=(scheda.spinta*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
        scheda.abs=(scheda.addominali*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
        scheda.legs=(scheda.gambe*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
        scheda.save()
    if str(blocco.esercizio.tipo)=='gambe':
        scheda.gambe -=1
        scheda.pull=(scheda.tirata*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
        scheda.push=(scheda.spinta*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
        scheda.abs=(scheda.addominali*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
        scheda.legs=(scheda.gambe*100)/(scheda.tirata+scheda.spinta+scheda.addominali+scheda.gambe)
        scheda.save()
   

    blocco.delete()
    return HttpResponseRedirect(f"/schedario/{scheda.slug}")


# -------------- TIMER ---------------------

def timer(request,slug,id):
    nome=Schedario.objects.get(slug=slug)
    blocco=Blocco.objects.get(nome_scheda=nome,id=id)
    context={"blocco":blocco,"scheda":nome}
    return render(request,"timer.html",context)