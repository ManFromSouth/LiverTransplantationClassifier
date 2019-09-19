from django.contrib import admin
from .models import male_lethal,female_lethal,male_compl,female_compl,point

# Register your models here.
admin.site.register(male_lethal)
admin.site.register(female_lethal)
admin.site.register(male_compl)
admin.site.register(female_compl)
admin.site.register(point)