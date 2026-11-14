from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from apps.users.models import CustomUser


class TailwindFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # Adiciona as classes do Tailwind em inputs
            if isinstance(
                field.widget,
                (
                    forms.TextInput,
                    forms.EmailInput,
                    forms.PasswordInput,
                    forms.Select,
                    forms.NumberInput,
                ),
            ):
                field.widget.attrs.update({
                "class": (
                    "w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm"
                    " focus:outline-none focus:ring-2 focus:ring-green-500"
                    " focus:border-green-500 text-sm bg-white"
                )
                })

class CustomAuthenticationForm(AuthenticationForm):
    """Formulário de login customizado para aplicar classes do Tailwind

    em seus campos de username e password.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                "class": (
                    "w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm"
                    " focus:outline-none focus:ring-2 focus:ring-green-500"
                    " focus:border-green-500 text-sm bg-white"
                )
            })


class CustomUserCreationForm(TailwindFormMixin, UserCreationForm):
    """Formulário oficial de criação de usuário do Django estendido

    para suportar o CustomUser do Food Bridge com os campos customizados.
    """

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            "username",
            "email",
            "role",
            "phone",
            "address",
            "latitude",
            "longitude",
        )


class CustomUserChangeForm(TailwindFormMixin, UserChangeForm):
    """Formulário de alteração de usuário para o Django Admin."""

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
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
        )