from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, MyTokenObtainPairView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
]

urlpatterns = format_suffix_patterns(urlpatterns)