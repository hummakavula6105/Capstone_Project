from rest_framework import serializers
from .models import User
from .models import Request
from .models import User_Requests

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','user_id','name', 'email_address', 'isAdmin', 'isApprover']
        depth = 1

    user_id = serializers.IntegerField(write_only=True)


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id','date_requested','date_closed','area','description','is_approved','is_rejected']
        depth = 1

    request_id = serializers.IntegerField(write_only=True)


class UserRequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Requests
        fields = ['id','row_id','request_id','user_id']
        depth = 1