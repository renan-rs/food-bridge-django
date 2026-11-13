from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Define quais formulários o admin deve usar para criar e editar
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = [
        "username",
        "email",
        "role",
        "is_verified",
        "is_staff",
    ]

    list_filter = ['role', 'is_verified', 'is_staff', 'is_active']
    actions = ["verify_users"] 

    @admin.action(description="Aprovar/Verificar usuários selecionados")
    def verify_users(self, request, queryset):
        updated_count = queryset.update(is_verified=True)
        self.message_user(
            request,
            f"{updated_count} usuário(s) foram verificados com sucesso.",
        )

    # Campos que aparecem na tela de EDIÇÃO de um usuário existente
    fieldsets = UserAdmin.fieldsets + (
        (
            "Informações Adicionais (Marketplace)",
            {
                "fields": (
                    "role",
                    "phone",
                    "address",
                    "latitude",
                    "longitude",
                    "is_verified",
                )
            },
        ),
    )

    # Campos que aparecem na tela de CRIAÇÃO de um novo usuário no admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Informações Adicionais (Marketplace)",
            {
                "fields": (
                    "role",
                    "phone",
                    "address",
                    "latitude",
                    "longitude",
                    "is_verified",
                )
            },
        ),
    )
