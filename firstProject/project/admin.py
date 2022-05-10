from django.contrib import admin

from project.models import Person, Musician, Album

admin.site.register(Person)
admin.site.register(Musician)
admin.site.register(Album)

from project.models import Students, Teacher, Group, GroupStudents
admin.site.register(Teacher)
admin.site.register(Students)
# admin.site.register(Group)
admin.site.register(GroupStudents)


@admin.register(Group)
class Groups(admin.ModelAdmin):
    list_display = ('id', 'title', 'teacher', 'list_of_students')

    def list_of_students(self, obj):
        qs = GroupStudents.objects.filter(group=obj.id)
        res = []
        for x in qs:
            x = str(x)[:-16]
            res.append(x)
        if not res:
            res = 'No students'
        return res

