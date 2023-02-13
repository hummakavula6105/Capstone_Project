from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Request
from serializers import MyChangeRequestSerializer
from serializers import RequestSerializer
from serializers import MyChangeRequestSerializer
from serializers import AdminsSerializers
from serializers import ApproversSerializer
from serializers import Edit_Request


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_requests():
    requests = Request.objects.all()
    serializer = RequestSerializer(requests, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_request(request):
    serializer = RequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_change_requests(request):
    serializer=MyChangeRequestSerializer(data=request.user.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
    return Response(serializer.data)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_request(request):
    serializer = EditRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def admin(request):
    serializer = AdminsSerializers(data=request.user.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def approver(request):
    serializer = ApproversSerializer(data=request.user.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)