from django.urls import path
from change_request import views

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('all/', views.get_all_requests),
    path('new/', views.new_request),
    path('<int:user_id>', views.my_change_requests),
    path('<int:request_id>/edit_request', views.edit_request),
    path('<int:request_id>/approve_or_reject_request/', views.approve_or_reject_request),
    # path('', graphs),
    # path('', users),
]