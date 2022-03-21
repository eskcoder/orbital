from tkinter.tix import Tree
from django.db import models

# Create your models here.
class Item(models.Model):
    itemname = models.CharField(max_length=255)
    itemcatagory = models.CharField(max_length=255)
    itemquantity = models.IntegerField()
    status = models.CharField(max_length=255)
    approverstatus = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
 