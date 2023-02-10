from django.shortcuts import render
from category.models import *
from .models import *
# Create your views here.
# list function ...........................
def List(r):
    return render(r,'book/index.html')

# Add function...................................

def Add(r):
    context={}
    context['categories'] = Catagory.objects.all()
    if(r.method=='GET'):
        return render(r, 'book/add.html',context)
    else:
        print(r.POST)
        Book.objects.create(name=r.POST['bookname'],publisher=r.POST['bookpublisher'],catagory=Catagory.objects.get(id=r.POST['bookCatagory']))
        return render(r, 'book/add.html', context)