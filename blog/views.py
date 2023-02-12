from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib import messages
from blog.forms import New_projectforms
from blog.models import Projetos



def index(request):
    return render(request,'blog/index.html')

def projects(request):
    projetos = Projetos.objects.all()
    return render(request,'blog/projects.html',{'Projetos': projetos})

def contact(request):
    return render(request,'blog/contact.html')

def project(request,projeto_id):
    projeto = get_object_or_404(Projetos,pk=projeto_id)
    return render(request,'blog/project.html',{'projeto':projeto})

@permission_required('blog.add_projeto',raise_exception=False,login_url='login')
def novoprojeto(request):
    if request.method != 'POST':
        form = New_projectforms()
        return render(request,'blog/novoprojeto.html',{'form': form})
    form = New_projectforms(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request,'Projeto adicionado')
        return render(request,'blog/novoprojeto.html',{'form': form})
    else:
        messages.error(request,'Projeto não valido!')
        return render(request,'blog/novoprojeto.html',{'form': form})