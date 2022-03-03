from django.urls import path

from .views import *

app_name = "users"

urlpatterns = [
    path('signup/', UserCreateView.as_view(), name="api-signup"),
    path('login/', LoginView.as_view(), name="api-login"),
    path('logout/', Logout.as_view(), name="api-logout"),
]
