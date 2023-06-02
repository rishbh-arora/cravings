from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    gender = (
        ("Male", "M")
        ("Female", "F")
    )

    user_type = (
        ("Student", "S")
        ("Mess", "M")
    )

    blocks = (
        ("A", "A")
        ("B-annex", "B-annex")
        ("B", "B")
        ("C", "C")
        ("D", "D")
        ("D-annex", "D-annex")
        ("E", "E")
        ("F", "F")
        ("G", "G")
        ("H", "H")
        ("J", "J")
        ("K", "K")
        ("L", "L")
        ("M", "M")
        ("MH - M-annex", "M-annex")
        ("N", "N")
        ("P", "P")
        ("Q", "Q")
        ("R", "R")
        ("GH - A", "GHA")
        ("GH - B", "GHB")
        ("GH - C", "GHC")
        ("GH - D", "GHD")
        ("GH - D-annex", "GHDA")
        ("GH - E", "GHE")
        ("GH - F", "GHF")
        ("GH - G", "GHG")
        ("GH - H", "GHH")
    )

    user_type = models.CharField(choices = user_type, max_length=9, default="M")
    pno = models.CharField(max_length=10)
    due = models.IntegerField(default=0)
    gender = models.CharField(choices=gender, max_length=5, default="M")
    block = models.CharField(choices=blocks, max_length=12, default="MHA")