from django.urls import path
from change_request import views

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('', views.new_request),
    path('', views.open_pending_requests),
    path('', views.past_requests),
    path('', views.my_change_requests),
    path('', views.my_tasks),
    path('', views.graphs),
    path('', views.cross_functional_teams),
]