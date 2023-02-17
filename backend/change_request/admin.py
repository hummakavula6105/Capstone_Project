from django.contrib import admin
from .models import User
from .models import Area
from .models import Request
from .models import Approvers
from .models import Admins
from .models import My_Change_Requests
from .models import Edit_Request

# Register your models here.

admin.site.register(User)
admin.site.register(Area)
admin.site.register(Request)
admin.site.register(Approvers)
admin.site.register(Admins)
admin.site.register(My_Change_Requests)
admin.site.register(Edit_Request)