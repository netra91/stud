from django.contrib import admin
from studcourseregapp.models import student,course
# Register your models here.
#admin.site.register(student)

admin.site.register(course)
@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display=('usn','name','sem')
    ordering=('usn',)
    search_fields=('name',)