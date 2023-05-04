from django.contrib import admin
from .models import student
class studentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']
admin.site.register(student,studentAdmin)
