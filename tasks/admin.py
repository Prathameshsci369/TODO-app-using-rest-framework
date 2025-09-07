from django.contrib import admin

# Register your models here.
from .models import Task 

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completed', 'created_at' )
    list_filter = ('completed',)
    search_fields = ('title', 'description')