from django.contrib import admin
from  .models import Project

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'description', 'url')
    ordering = ('title', 'created')
    search_fields = ('title','description','url')
    date_hierarchy = 'updated'
    list_filter = ('title','url')

# Register your models here.
admin.site.register(Project, ProjectAdmin)
