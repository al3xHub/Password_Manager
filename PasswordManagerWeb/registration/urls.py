from django.urls import path
from .views import SignUpView, ProfileUpdate, EmailUpdate, DeleteUser

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('profile/', ProfileUpdate.as_view(), name="profile"),
    path('profile/email/', EmailUpdate.as_view(), name="profile_email"),
    path('delete_user/<int:pk>/', DeleteUser.as_view(), name="delete_user"),
]