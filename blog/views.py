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
    forms = New_projectforms()
    if request.method == 'POST':
        messages.warning(request,'teste')
        projetos = New_projectforms(request.POST)
        if projetos.is_valid():
            try:
                novo_projeto = Projetos(
                nome = projetos['project_name'].value(),
                imagem = projetos['project_img'].value(),
                legenda = projetos['project_legend'].value(),
                descricao = projetos['project_descricao'].value(),
                link_projeto = projetos['project_link'].value(),

                )
                novo_projeto.save()
                messages.success(request,'Projeto Adicionado!')
            except Exception as erro:
                messages.error(request,f'Ocorreu Um Erro! {erro}')
    return render(request,'blog/novoprojeto.html',{'form':forms})