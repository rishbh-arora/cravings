from django.db import models
from django.contrib.auth.models import AbstractUser

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

    user_type = models.CharField(choices = user_type, max_length=9, default="M")
    pno = models.CharField(max_length=10)
    due = models.PositiveIntegerField()
    gender = models.CharField(choices=gender, max_length=6, default="M")
    block = models.CharField(choices=blocks, max_length=12, default="MHA")

    