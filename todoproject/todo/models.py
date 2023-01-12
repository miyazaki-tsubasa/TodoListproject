from django.db import models

# Create your models here.

CHOICE = (('danger','high'),('warning','normal'),('primary','low'))

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices = CHOICE,
        null =True
     )
    duedate = models.DateField()

#管理画面のobjectの表示をタイトルと一致して表示
    def __str__(self):
        return self.title



