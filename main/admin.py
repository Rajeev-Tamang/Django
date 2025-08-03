from django.contrib import admin
from .models import Task,Student,School,Address, Grade,SudentProfile, Parent
# from django.contrib.contenttypes.admin import GenericTabularInline

# Register your models here.

admin.site.register(Task)
admin.site.register(School)
# admin.site.register(Student)
admin.site.register(Address)
admin.site.register(Grade)
admin.site.register(SudentProfile)
admin.site.register(Parent)




class studentProfileInline(admin.StackedInline):
    model = SudentProfile


class AdminInline(admin.ModelAdmin):
    inlines = [
        studentProfileInline,
    ]
    list_display=["name", "address","grade", "roll_num"]
    search_fields=["name"]
    list_filter=["grade"]
admin.site.register(Student, AdminInline)


