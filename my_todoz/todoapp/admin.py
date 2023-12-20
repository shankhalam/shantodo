from django.contrib import admin
from.models import Add_task


# To view model as table in dashboard
class TaskTable(admin.ModelAdmin):
    list_display = ('id', 'task', 'priority', 'date')


# Register your models here.
admin.site.register(Add_task, TaskTable)