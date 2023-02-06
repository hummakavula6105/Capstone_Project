from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import User
from .models import Request
from .models import User_Requests
from .serializers import UserSerializer
from .serializers import RequestSerializer
from .serializers import UserRequestsSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_requests(request):
    requests = Request.objects.all()
    serializer = RequestSerializer(requests, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_requests(request):

    if request.method == 'POST':
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        requests = Request.objects.filter(request_id=request.query_params.get("request_id"))
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data)
