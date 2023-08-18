from rest_framework.response import Response
from rest_framework import viewsets  
from rest_framework.permissions import AllowAny, IsAuthenticated 
from django.contrib import messages
from base.models import User
from .serializers import UserSerializer



class GetUserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pemission_classes= [AllowAny]