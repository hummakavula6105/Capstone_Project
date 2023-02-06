from django.urls import path
from change_request import views

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('', views.user_requests),
    path('all/', views.get_all_requests),
]