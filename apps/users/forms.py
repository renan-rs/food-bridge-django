from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from apps.users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        models = CustomUser
        fields = (
            "username",
            "email",
            "role",
            "phone",
            "address",
            "latitude",
            "longitude",
        )

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "role",
            "phone",
            "address",
            "latitude",
            "longitude",
            "is_verified",
        )