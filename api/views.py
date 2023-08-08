from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from base.models import User
from .serializers import UserSerializer


@api_view(['POST'])
def login(request):

    if request.method == 'POST':
        username = request.POST.get(username=username)
        password = request.POST.get(password=password)

    try:
        user = User.objects.get(username=username)
    except:
        messages.error(request, "username not correct")

    user = authenticate(request, username = username, password = password)
#if the user exist then>>>
# here two auth importedd are used
    if user is None:
        login(request,user)

        


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid:
        serializer.save()
    return Response(serializer.data)