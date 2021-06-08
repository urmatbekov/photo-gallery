from django.shortcuts import render
from .models import Image
from .forms import GalleryForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# Create your views here.
def gallery(request):
    images = Image.objects.all()
    return render(request,"gallery/gallery.html",{"images":images})

def addImage(request):
    form = GalleryForm()
    if request.method == "POST":
        form = GalleryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request,"gallery/add.html",{"form":form})
def detail_gallery(request,id):
    image = Image.objects.get(id=id)
    return render(request,"gallery/detail.html",{"image":image})

def auth(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect("/")
    return render(request,"gallery/login.html",{"form":form})

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request,"gallery/register.html",{"form":form})
    

