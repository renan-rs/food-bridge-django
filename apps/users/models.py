from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Administrador"
        DONOR = "DONOR", "Doador"
        RECEIVER = "RECEIVER", "Receptor"

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.RECEIVER)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    is_verified = models.BooleanField(
        default=False,
        help_text="Indica se o usuário foi verificado/aprovado pela moderação (essencial para doadores e ONGs).",
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"