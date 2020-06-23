from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import *

# pyjwt decode --no-verify <TOKEN>
# import jwt
# jwt.decode('<TOKEN>', verify=False)

# jwt.encode(<PAYLOAD>, '<SECRET_KEY>', algorithm=['HS256']) => <TOKEN>
# jwt.decode('<TOKEN>','<SECRET_KEY>',algorithms=['HS256']) => <PAYLOAD>

# import time
# int(time.time())

urlpatterns = [
    path('login/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('login/token/custom/', MyTokenObtainPairView.as_view()),
    path('hello/', Hello.as_view()),  
]