from django.contrib import admin
from .models import Task,Address,School,Student,StudentProfile

# Register your models here.
admin.site.register(Task)
admin.site.register(Address)
admin.site.register(School)
# admin.site.register(Student)
admin.site.register(StudentProfile)

class StudentProfileInline(admin.StackedInline):
    model=StudentProfile

class StudentModelAdmin(admin.ModelAdmin):
    inlines=[
        StudentProfileInline
    ]
    search_fields=["name"]
    list_display=["name","address","school"]
    list_filter=["school"]
admin.site.register(Student,StudentModelAdmin)