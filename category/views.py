from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

# list function ..............................
def List(req):
    context={}
    context['catagories']=Catagory.objects.all()
    for cat in context['catagories']:
        print(cat.name)

    return render(req,'Catagory/index.html',context)
# Update function ..............................
def Update(req,catid):
    context = {}
    if(req.method=='GET'):
        #get category object from db
        #select * from catatgory_catagory where id=catid
        cat=Catagory.objects.get(id=catid)
        context['cat']=cat
        return render(req,'category/Update.html',context)
    else:
        Catagory.objects.filter(id=catid).update(name=req.POST['catgoryname'])
        #context['catagories']=Catagory.objects.all()
        #return render(req, 'category/index.html',context)
        return HttpResponseRedirect('/')

# Add function ..............................
def Add(req):
    if(req.method=='GET'):
        context={}
        context['form']=CatagoryForm()
        return  render(req,'category/Add.html',context)
    else:
        #form=CategoryForm2(req.POST)
        print(req.POST)
        data=req.POST
        print(data['catgoryname'])

        Category.objects.create(name=req.POST['catgoryname'])
        #form.save()
        '''
        catobj=Catagory()
        catobj.name=data['catgoryname']
        catobj.save()
        '''
        #insert in db
        context={}
        context['msg']='added'
        return render(req, 'category/Add.html',context)