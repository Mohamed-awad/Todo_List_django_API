from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer


class UserCreateView(generics.CreateAPIView):
    """
    View to create User.
    """
    lookup_field = 'pk'
    serializer_class = UserSerializer
    permission_classes = []

    # override create to return custom response
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': status.HTTP_200_OK,
            'message': 'user created successfully',
            'data': response.data
        })


class LoginView(ObtainAuthToken):
    """
    View to generate User Token.
    """
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'status': status.HTTP_200_OK,
            'message': 'token generated successfully',
            'data': {
                'token': token.key,
                'user_id': user.pk,
                'username': user.username
            }
        })


class Logout(APIView):
    """
    view for logout
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response({
            "status": status.HTTP_200_OK,
            'message': 'logout successfully',
            'data': {}
        })



