from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .models import Request
from .models import Approvers
from .serializers import MyChangeRequestSerializer
from .serializers import RequestSerializer
from .serializers import AdminsSerializers
from .serializers import ApproversSerializer
from .serializers import EditRequestSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_requests(request):
    request = request.query_params.get('request')
    queryset = Request.objects.all()
    if request:
        queryset = queryset.filter(request__=request)
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
def approve_or_reject_request(request):
    try:
        request_id = int(request.data['request_id'])
        approver = Approvers.objects.get(request_id=request_id, user=request.user)
        is_approved = request.data.get('is_approved', False)
        is_rejected = request.data.get('is_rejected', False)
        if is_approved and is_rejected:
            return Response({'message': 'Cannot approve and reject request at the same time'}, status=status.HTTP_400_BAD_REQUEST)
        approver.is_approved = is_approved
        approver.is_rejected = is_rejected
        approver.save()
        return Response({'message': 'Request updated'}, status=status.HTTP_200_OK)
    except (KeyError, ValueError, Approvers.DoesNotExist):
        return Response({'message': 'Invalid request ID or user not authorized'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_change_requests(request, user_id):
    user=user.objects.get(id=user_id)
    if user:
        requests = Request.objects.get(owner_id=user_id)
        serializer=MyChangeRequestSerializer(requests, many=True)
        return Response(serializer.data)
    else:
        return "None"
    

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def edit_request(request):
    print(
        'User', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'GET':
        request = Request.objects.filter(request_id=request.user.id)
        serializer = EditRequestSerializer(request)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EditRequestSerializer(request_id=request.user.id)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(EditRequestSerializer.data, status=status.HTTP_201_CREATED)
        return Response(EditRequestSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


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