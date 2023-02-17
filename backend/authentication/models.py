from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.http import HttpResponse

# class AdminAllowedPermissionTo:
#     user = 'user',
#     graphs = 'graphs',
#     ADMIN_PERMISSION_AREAS = [
#         ('user', 'user'),
#         ('graphs', 'graphs'),
#     ]

#     def admin_view(admin_request):
#         admin_user = admin_request.admin_user
#         if admin_user.isAdmin == True:
#             return HttpResponse("Access Granted")
#         elif admin_user.area in [area for area, _ in AdminAllowedPermissionTo.ADMIN_PERMISSION_AREAS]:
#             return HttpResponse("Access Granted")
#         else:
#             return HttpResponse("Unauthorized")


class User(AbstractUser):
    pass


    '''
    This is a custom version of the built in User class
    It contains all of the built in fields and functionality of the standard User
    You can add fields here for any additional properties you want a User to have
    This is useful for adding roles (Customer and Employee, for example)
    For just a few roles, adding boolean fields is advised
    '''
    # Example (note import of models above that is commented out)
    # this will add a column to the user table
    # is_student = models.BooleanField('student status', default=False)
