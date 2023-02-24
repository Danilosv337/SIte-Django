from django.shortcuts import render,redirect
from usuarios.forms import Loginforms
from django.contrib import auth
from django.contrib import messages

# Create your views here.
def login(request):
    form = Loginforms()
    if request.method == 'POST':
        form = Loginforms(request.POST)
        if form.is_valid():
           nome = form['username'] .value()
           senha = form['senha'].value()
        usuario = auth.authenticate(
            request,
            username  = nome,
            password = senha
        )
        if usuario is not None:
            auth.login(request,usuario)
            messages.success(request,'Login Bem Sucedido')
            return redirect('index')
        else:
            messages.error(request,'Usuário ou senha inválidos!')
            return redirect('login')
    return render(request,'usuarios/login.html',{'form': form})
    # return render (request,'usuarios/login.html',{'form':form})
def logout(request):
    auth.logout(request)
    return redirect('login')
