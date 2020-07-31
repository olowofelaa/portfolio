from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from projects.models import Project, About

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

def index(request):
    return render(request, 'index.html', {})

def about(request):
    abt = About.objects.all()
    context = {
        'abt': abt
    }
    return render(request, 'about.html',  context)

def contact(request):
    return render(request, 'contact.html', {})
