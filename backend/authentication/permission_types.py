# from django.http import HttpResponse
# from models import Request

# class AdminAllowedPermissionTo:
#     users = 'users',
#     graphs = 'graphs',
#     ADMIN_PERMISSION_AREAS = [
#         ('users', 'users'),
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


# class  ApproverAllowedPermissionTo:
#     approve = 'approve',
#     reject = 'reject',

#     def approver_view(approver_request):
#         approver_user = approver_request.approver_user
#         if approver_user.has_perm('change_request.approve'):
#             return Request.is_approved
#         elif approver_user.has_perm('change_request.reject'):
#             return Request.is_rejected
#         else:
#             return HttpResponse("Unauthorized")