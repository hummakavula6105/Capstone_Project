from rest_framework import serializers
from .models import User
from .models import Area
from .models import Approvers
from .models import Admins
from .models import Request
from .models import My_Change_Requests
from .models import Edit_Request


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_id', 'first_name', 'last_name', 'email_address', 'isAdmin', 'isApprover']
        depth = 1

    user_id = serializers.IntegerField(write_only=True)


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['id', 'area']
        depth = 1


class ApproversSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approvers
        fields = ['id', 'user_id', 'first_name', 'last_name', 'email_address']
        depth = 1


class AdminsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Admins
        fields = ['id', 'user_id', 'first_name', 'last_name', 'email_address']
        depth = 1


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id', 'request_id', 'date_requested', 'date_closed', 'area', 'description', 'is_approved', 'is_rejected']
        depth = 1

    request_id = serializers.IntegerField(write_only=True)


class MyChangeRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = My_Change_Requests
        fields = ['id', 'row_id', 'request_id', 'user_id']
        depth = 1


    class EditRequestSerializer(serializers.ModelSerializer):
        class Meta:
            model = Edit_Request
            fields = ['id', 'row_id', 'request_id', 'user_id', 'date_requested', 'date_closed', 'area', 'description']
            depth = 1