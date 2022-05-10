from django.db import models
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    groups_num = models.IntegerField()
    def __str__(self): return f'{self.name} {self.last_name}'

class Groups(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=50)
    students_num = models.IntegerField()
    def __str__(self): return f'{self.teacher}: {self.group_name}'

class Student(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self): return f'{self.name} {self.last_name}: {self.teacher}'




