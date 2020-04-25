from django.shortcuts import render
from django.http import HttpResponse
from .models import Experience, Skills, Certificate, Education, Project, Contact

def index(request):

	eduo = Education.objects.all()
	expo = Experience.objects.all()
	skill = Skills.objects.all()
	certi = Certificate.objects.all()
	proj = Project.objects.all()
	conta = Contact.objects.all()

	return render(request,'index.html', {'edu': eduo,'exp': expo, 'skills': skill, 'certif': certi, 'pro': proj, 'cont': conta})

# Create your views here.
