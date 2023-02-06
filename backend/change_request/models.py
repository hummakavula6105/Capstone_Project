from django.db import models
from authentication.models import User

# Create your models here.

class User(models.Model):
    id = models.IntegerField(primary_key=True)

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    isAdmin = models.BooleanField()
    isApprover = models.BooleanField()



class Request(models.Model):
    id = models.IntegerField(primary_key=True)

    date_requested = models.DateField()
    date_closed = models.DateField()
    area = models.IntegerField()
    description = models.CharField(max_length=800)
    is_approved = models.BooleanField()
    is_rejected = models.BooleanField()

    def __str__(self) -> str:
        return super(Request).__str__()



class User_Requests(models.Model):
    row_id=models.IntegerField(primary_key=True)
    request_id=models.ManyToManyField(Request)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super(User_Requests).__str__()