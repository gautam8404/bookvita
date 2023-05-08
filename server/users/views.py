from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, permissions

from .models import User
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer


# Create your views here.

class UserRegisterView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserRegisterSerializer
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        if not request.data:
            return Response({'error': 'No data provided'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'success': 'User registered successfully'}, status=status.HTTP_200_OK)


class UserLoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserLoginSerializer
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        if not request.data:
            return Response({'error': 'No data provided'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class RefreshTokenView(TokenRefreshView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['post']


class UserView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = [JWTAuthentication]
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    authentication_classes = [JWTAuthentication]
    serializer_class = UserSerializer
    lookup_field = 'username'
    queryset = User.objects.all()

    def put(self, *args, **kwargs):
        return self.partial_update(*args, **kwargs)


# TODO: remove is_authenticated
from django.shortcuts import HttpResponse


class is_authenticated(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        if request.user.is_authenticated:
            return Response({'is_authenticated': True}, status=status.HTTP_200_OK)
        else:
            return Response({'is_authenticated': False}, status=status.HTTP_200_OK)


# TODO: Implement logout
class UserLogoutView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [JWTAuthentication]
    http_method_names = ['get']

    def get(self, request):
        return HttpResponse('Logged out')
