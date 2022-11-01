from urllib import request
from django.shortcuts import render,HttpResponse
from dummyapp.models import Userdetails
from dummyapp.forms import CustForm
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.

def indexpage(request):
    
    return render(request,'linitv2/index.html')


def productionpage(request):
    return render(request, 'linitv2/production.html')


def pumppage(request):
    return render(request, 'linitv2/pump.html')

def valvepage(request):
    return render(request, 'linitv2/valve.html')

def CNCpage(request):
    return render(request, 'linitv2/CNC.html')

def pipepage(request):
    return render(request, 'linitv2/pipe.html')

def stainlesssteelpage(request):
    return render(request, 'linitv2/stainlesssteel.html')    

def rubberpage(request):
    return render(request, 'linitv2/rubber.html')


def gallerypage(request):
    return render(request, 'linitv2/gallery.html')

def qualitypage(request):
    return render(request, 'linitv2/quality.html')

def rotterdampage(request):
    return render(request, 'linitv2/rotterdam.html')

def perfomancepage(request):
    return render(request, 'linitv2/perfomance.html')

def life_at_linitpage(request):
    return render(request, 'linitv2/life_at_linit.html')


def careerspage(request):
    return render(request, 'linitv2/careers.html')

def contactpage(request):
    if request.method=='POST':  
        form = CustForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            
            messages.success(request, 'Your form submitted successfully.')
            return redirect('contactpage')   
        else:
            return render(request, 'linitv2/contact.html',{'form':form})   
            
    else:
        form = CustForm(None)
    
    return render(request, 'linitv2/contact.html',{'form':form})



