from django.shortcuts import render,redirect
from django.contrib.auth import logout
# Create your views here.

def bem_vindo(request):
    return render(request,'index.html')



def my_logout(request):
    logout(request)
    return redirect('bem_vindo')
