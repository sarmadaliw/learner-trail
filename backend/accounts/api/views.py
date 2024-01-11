from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from django.urls import reverse

@api_view(["POST"])
@permission_classes([AllowAny])
def login_api(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        redirect_url = reverse("home") 
        return Response({"detail": "Successfully logged in.", "redirect_url": redirect_url}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(["POST"])
def register_api(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.data)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,
                                               password=request.data["password1"])
            if authenticated_user:
                login(request, authenticated_user)
                token, created = Token.objects.get_or_create(user=authenticated_user)
                return Response({"token": token.key}, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(["POST"])
def logout_api(request):
    if request.method == "POST":
        logout(request)
        return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)