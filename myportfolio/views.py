from django.shortcuts import render
from bio.models import Bio
from education.models import Degree
from skills.models import Skill
from experience.models import Project

def home(request):
    # 1. Fetch data from database
    bios = Bio.objects.all()
    degrees = Degree.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()

    # 2. Put data in context
    context = {
        'bios': bios,
        'degrees': degrees,
        'skills': skills,
        'projects': projects,
    }
    
    # 3. Send to template
    return render(request, 'index.html', context)

# MAKE SURE THERE IS NOTHING WRITTEN BELOW THIS LINE