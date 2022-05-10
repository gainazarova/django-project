from django.contrib import admin

from groups.models import Teacher, Student, Groups
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Groups)
