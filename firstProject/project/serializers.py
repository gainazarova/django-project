from rest_framework import serializers
from project.models import Group, GroupStudents, Students, Teacher


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'teacher', 'groups',)


class GroupStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupStudents
        fields = ('student',)


class GroupDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'teacher', 'groups')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['teacher'] = TeachersSerializer(
            Teacher.objects.get(id=instance.teacher.id)
        ).data

        keys = []
        for x in representation['groups']:
            keys.append(GroupStudentSerializer(GroupStudents.objects.get(id=x)).data)
        res = []
        for x in keys:
            res.append(StudentSerializer(Students.objects.get(id=x['student'])).data)
        representation['students'] = res
        representation.pop('groups')
        return representation


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('id', 'name', 'last_name',)


class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
