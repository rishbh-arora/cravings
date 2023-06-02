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
        ("MH - A", "MA"),
        ("MH - B-annex", "MBA"),
        ("MH - B", "MB"),
        ("MH - C", "MC"),
        ("MH - D", "MD"),
        ("MH - D-annex", "MD"),
        ("MH - E", "ME"),
        ("MH - F", "MF"),
        ("MH - G", "MG"),
        ("MH - H", "MH"),
        ("MH - J", "MJ"),
        ("MH - K", "MK"),
        ("MH - L", "ML"),
        ("MH - M", "MM"),
        ("MH - M-annex", "MMA"),
        ("MH - N", "MN"),
        ("MH - P", "MP"),
        ("MH - Q", "MQ"),
        ("MH - R", "MR"),
        ("GH - A", "GA"),
        ("GH - B", "GB"),
        ("GH - C", "GC"),
        ("GH - D", "GD"),
        ("GH - D-annex", "GDA"),
        ("GH - E", "GE"),
        ("GH - F", "GF"),
        ("GH - G", "GG"),
        ("GH - H", "GH"),
    )

    user_type = models.CharField(choices = user_type, max_length=9, default="S")
    regno = models.CharField(max_length=9, default="00BBS0000")
    pno = models.CharField(max_length=10)
    due = models.PositiveIntegerField(default=0)
    gender = models.CharField(choices=gender, max_length=6, default="M")
    block = models.CharField(choices=blocks, max_length=12, default="MHA")


class menu(models.Model):
    block = models.CharField(choices=CustomUser.blocks, max_length=12, default="MHA")
    item = models.CharField(max_length=50)
    rate = models.PositiveIntegerField()

    class Meta:
        def __str__(self) -> str:
            return 
    

class order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token_no= models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    item = models.ForeignKey(menu, on_delete=models.CASCADE)
    book_time = models.DateTimeField(default = datetime.datetime.now())
    exp_time = models.DateTimeField(default = datetime.datetime.now() + datetime.timedelta(minutes=25))
    total = models.FloatField()

class cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    item = models.ForeignKey(menu, on_delete=models.CASCADE)
    total = models.FloatField()
