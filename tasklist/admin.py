from django.contrib import admin
from .models import TaskList

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display=['user']

admin.site.register(TaskList, TaskAdmin)