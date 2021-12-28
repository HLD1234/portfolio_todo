from django.db import models

# Create your models here.
class ToDo(models.Model):
    date = models.DateField((""), auto_now=False, auto_now_add=False)
    title = models.CharField(max_length=200, blank=False, default="")
    detail = models.CharField(max_length=200, default="")
    complete = models.BooleanField(default=False)

    db_table = 'todo-list'