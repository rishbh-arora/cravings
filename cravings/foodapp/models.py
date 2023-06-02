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
        ("MH - A", "MHA")
        ("MH - B-annex", "MHBA")
        ("MH - B", "MHB")
        ("MH - C", "MHC")
        ("MH - D", "MHD")
        ("MH - D-annex", "MHDA")
        ("MH - E", "MHE")
        ("MH - F", "MHF")
        ("MH - G", "MHG")
        ("MH - H", "MHH")
        ("MH - J", "MHJ")
        ("MH - K", "MHK")
        ("MH - L", "MHL")
        ("MH - M", "MHM")
        ("MH - M-annex", "MHMA")
        ("MH - N", "MHN")
        ("MH - P", "MHP")
        ("MH - Q", "MHQ")
        ("MH - R", "MHR")
    )

    user_type = models.CharField(choices = user_type, max_length=9, default="M")
    pno = models.CharField(max_length=10)
    due = models.IntegerField(default=0)
    gender = models.CharField(choices=gender, max_length=5, default="M")
    block = models.CharField()
