from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')
    else:	         
        form = 	UserCreationForm()

    return render(request, "accounts/signup.html", {'form':form})

def login_view(request):
    if request.method == 'POST':
       	form = AuthenticationForm(data=request.POST)
       	if form.is_valid():
       	   user = form.get_user()
       	   login(request,user)	
           return redirect('/')   		
    else:
        form = AuthenticationForm()

    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
       err_msg = {
           "message" : 'You are logged out!'
        }
       logout(request)
       return render(request, "readbooks/error.html",err_msg)  	   	 	 	