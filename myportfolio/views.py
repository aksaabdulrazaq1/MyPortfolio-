from django.shortcuts import render
from bio.models import Bio
from education.models import Degree
from skills.models import Skill
from experience.models import Project

def home(request):
    context = {
        'bio': Bio.objects.first(),
        'degrees': Degree.objects.all(),
        'skills': Skill.objects.all(),
        'projects': Project.objects.all(),
    }
    return render(request, 'index.html', context)