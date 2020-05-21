from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import Hello

urlpatterns = [
    path('login/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', Hello.as_view()),  
]