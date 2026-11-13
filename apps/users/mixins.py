from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from apps.users.models import CustomUser

class DonorRequiredMixin(UserPassesTestMixin):
    """Permite acesso apenas a usuários com o role DOADOR."""

    def test_func(self):
        return (
            self.request.user.is_authenticated 
            and self.request.user.role == CustomUser.Role.DONOR
        )

class ReceiverRequiredMixin(UserPassesTestMixin):
    """Permite acesso apenas a usuários com o role RECEPTOR."""

    def test_func(self):
        return (
            self.request.user.is_authenticated 
            and self.request.user.role == CustomUser.Role.RECEIVER
        )

class VerifiedUserRequiredMixin(UserPassesTestMixin):
    """Permite acesso apenas a usuários que foram verificados pela moderação."""

    def test_func(self):
        return (
            self.request.user.is_authenticated 
            and self.request.user.is_verified
        )
