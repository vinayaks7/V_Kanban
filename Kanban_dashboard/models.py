import django


from django.db import models


class User_Table(models.Model):
    user_id = models.AutoField(primary_key=True,default="user")
    user_name = models.CharField(null=False, max_length=100,default="Vinayak")
    password = models.CharField(null=False,max_length=50,default="pass")

class Task_Table(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_desc = models.CharField(null=False, max_length=100,default="DESC")
    task_status = models.CharField(null=False, max_length=100,default="STATUS")
    task_priority = models.IntegerField(null=False,default="3")
    task_summary = models.CharField(null=False, max_length=50,default="SUMMARY")
    user_id = models.ForeignKey(User_Table,models.CASCADE,default= 1)
    task_deadline = models.DateField(null=False,default=django.utils.timezone.now)






