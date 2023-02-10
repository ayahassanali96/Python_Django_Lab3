from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from  django.views.decorators.http import require_http_methods
from django.views import View
from django.views.generic import ListView
class List(ListView):
    model = MyUser

class Loginview(View):
    def get(self,req):
        return render(req, 'Login.html')
    def post(self,req):
        u = MyUser.objects.filter(username=req.POST['username'], password=req.POST['password'])
        authuser = authenticate(username=req.POST['username'], password=req.POST['password'])
        print(authuser)
        if (u[0] is not None and authuser is not None):
            req.session['userid'] = u[0].id
            req.session['username'] = u[0].username
            login(req, authuser)
            return HttpResponseRedirect('/')
        else:
            context = {}
            context['error'] = 'username or password wong'
            return render(req, 'Login.html', context)

def secondRegistration(req):
    if(req.method=='POST'):
        x=MyUser.objects.create(
            username=req.POST['username'],
            password=req.POST['password'],
            email=req.POST['email']
        )
        User.objects.create_superuser(username=req.POST['username']
                                      , password=req.POST['password'],
                                      email=req.POST['email'])

        req.session['userid']=x.id
        req.session['username']=x.username

        return  render(req,'Book/index.html')
    else:
        return render(req, 'Register.html' )
def secondlogin(req):
    req.session.clear()
    return HttpResponseRedirect('Login')


@require_http_methods(['GET'])
def secondlogin(req):
    if (req.method == 'GET'):
        return render(req, 'Login.html')
    else:
        u = MyUser.objects.filter(username=req.POST['username'], password=req.POST['password'])
        authuser=authenticate(username=req.POST['username'],password=req.POST['password'])
        print(authuser)
        if (u[0] is not None and authuser is not None):
            req.session['userid'] = u[0].id
            req.session['username'] = u[0].username
            login(req,authuser)
            return HttpResponseRedirect('/')
        else:
            context = {}
            context['error'] = 'username or password wong'
            return render(req, 'Login.html', context)


























# Create your views here.
def mylogin(req):
    return render(req,'Login.html')
def mylogout(req):
    req.session.clear()
    return HttpResponseRedirect('Login')
def myregister(req):
    if(req.method=='GET'):
        return render(req,'Register.html')
    else:
        x=MyUser.objects.create(username=req.POST['username'],password=req.POST['password'])
        User.objects.create_user(username=req.POST['username'],password=req.POST['password'],email='asd@yahoo.com')
        req.session['userid']=x.id
        req.session['username']=x.username
        return HttpResponseRedirect('/')
