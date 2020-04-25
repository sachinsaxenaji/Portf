from django.contrib import admin
from .models import Education, Experience, Skills, Certificate, Project
from .models import Contact

admin.site.register(Education)

admin.site.register(Experience)

admin.site.register(Skills)

admin.site.register(Certificate)

admin.site.register(Project)

admin.site.register(Contact)
# Register your models here.
