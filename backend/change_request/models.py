from django.db import models
from authentication.models import AbstractUser

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    isApprover = models.BooleanField(default=False)
    isAdmin = models.BooleanField(default=False)


class Area(models.Model):
    ETM = 'ETM'
    CD6R_2pc = 'CD6R 2pc'
    P702 = 'P702'
    Supermarket = 'Supermarket'
    LD71 = 'LD71'
    AREA_CHOICES = [
        (ETM, 'ETM'),
        (CD6R_2pc, 'CD6R 2pc'),
        (P702, 'P702'),
        (Supermarket, 'Supermarket'),
        (LD71, 'LD71'),
    ]

class Request(models.Model):
    id = models.AutoField(primary_key=True)
    date_requested = models.DateField()
    date_closed = models.DateField()
    area = models.CharField(
        max_length=20,
        choices=Area.AREA_CHOICES,
    )
    description = models.CharField(max_length=800)
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    

class Approvers(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Admins(models.Model):
    user = models.ForeignKey(AbstractUser, on_delete=models.CASCADE)


class User_Requests(models.Model):
    row_id = models.AutoField(primary_key=True)
    request = models.ForeignKey(Request, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(AbstractUser, on_delete=models.CASCADE)
    

class Edit_Request(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    edit = models.CharField(
        max_length=800,
    )