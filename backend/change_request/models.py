from django.db import models
from authentication.models import User

# Create your models here.

class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    request_id = models.IntegerField(primary_key=User)
    date_requested = models.DateField()
    expiration_date = models.DateField()
    area = models.CharField(
        max_length=20,
        choices=Area.AREA_CHOICES,
    )
    reason_for_request = models.CharField(max_length=800)
    description_of_change = models.CharField(max_length=800)
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    

class Approvers(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Admins(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class My_Change_Requests(models.Model):
    row_id = models.AutoField(primary_key=True)
    request = models.ForeignKey(Request, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Edit_Request(models.Model):
    edit_request = models.ForeignKey(Request, on_delete=models.CASCADE)
    edit = models.CharField(
        max_length=800,
    )