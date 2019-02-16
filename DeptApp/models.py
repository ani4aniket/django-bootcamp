from django.db import models

# Create your models here.


class Student(models.Model):
    name=models.CharField(max_length=30)
    e_mail=models.EmailField(max_length=254)
    contact_no=models.CharField(max_length=10)
    stream=models.CharField(max_length=4,choices=[
                                                    ('IT','Information Technology'),
                                                    ('CSE','Computer Science Engineering'),
                                                ]
                           )
    date_of_birth=models.DateField()

    def __str__(self):
        return self.name

    # from django.urls import reverse

    # def get_absolute_url(self):
    #     return   reverse('std_detail',kwargs={'pk':self.id})  