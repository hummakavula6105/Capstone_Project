from django.urls import path
from change_request.views import *

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('', get_all_requests),
    path('new', new_request),
    # path('', my_change_requests),
    # path('', edit_request),
    # path('', graphs),
    # path('', users),
]