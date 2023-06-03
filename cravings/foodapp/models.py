from django.db import models
from django.contrib.auth.models import AbstractUser

import datetime

class CustomUser(AbstractUser):

    gender = (
        ("Male", "M"),
        ("Female", "F"),
    )

    user_type = (
        ("Student", "S"),
        ("Mess", "M"),
    )

    blocks = (
        ("Base", "Base"),
        ("MA", "MA"),
        ("MB", "MB"),
        ("MBA", "MBA"),
        ("MC", "MC"),
        ("MD", "MD"),
        ("MD", "MD"),
        ("ME", "ME"),
        ("MF", "MF"),
        ("MG", "MG"),
        ("MH", "MH"),
        ("MJ", "MJ"),
        ("MK", "MK"),
        ("ML", "ML"),
        ("MM", "MM"),
        ("MMA", "MMA"),
        ("MN", "MN"),
        ("MP", "MP"),
        ("MQ", "MQ"),
        ("MR", "MR"),
        ("GA", "GA"),
        ("GB", "GB"),
        ("GC", "GC"),
        ("GD", "GD"),
        ("GDA", "GDA"),
        ("GE", "GE"),
        ("GF", "GF"),
        ("GG", "GG"),
        ("GH", "GH"),
    )

    user_type = models.CharField(choices = user_type, max_length=9, default="S")
    regno = models.CharField(max_length=9, default="00BBS0000")
    pno = models.CharField(max_length=10)
    due = models.PositiveIntegerField(default=0)
    gender = models.CharField(choices=gender, max_length=6, default="M")
    block = models.CharField(choices=blocks, max_length=12, default="MA")

class menu(models.Model):
    block = models.CharField(choices=CustomUser.blocks, max_length=12, default="MA")
    item = models.CharField(max_length=50)
    rate = models.PositiveIntegerField()

    def __str__(self):
        return self.item
    

class order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    token_no= models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    item = models.ForeignKey(menu, on_delete=models.CASCADE)
    book_time = models.DateTimeField(default = datetime.datetime.now())
    exp_time = models.DateTimeField(default = datetime.datetime.now() + datetime.timedelta(minutes=5))
    total = models.PositiveIntegerField()
    valid = models.BooleanField(default=(book_time < exp_time))
    ready = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
