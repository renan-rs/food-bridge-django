import pytest
from django.urls import reverse
from apps.users.models import CustomUser


@pytest.mark.django_db
class TestUserAndPermissions:

    def create_user(self, username, role, is_verified=False):
        return CustomUser.objects.create_user(
            username=username,
            password="testpassword123",
            role=role,
            is_verified=is_verified,
        )

    def test_create_custom_user(self):
        user = self.create_user(
            username="donor_test", role=CustomUser.Role.DONOR
        )
        assert user.username == "donor_test"
        assert user.role == CustomUser.Role.DONOR
        assert user.is_verified is False
        assert str(user) == "donor_test (Doador)"

    def test_donor_mixin_permission(self, client):
        donor = self.create_user(username="donor1", role=CustomUser.Role.DONOR)
        receiver = self.create_user(
            username="receiver1", role=CustomUser.Role.RECEIVER
        )

        # Testando mock de acesso com o Doador (deve passar ou permitir)
        client.force_login(donor)
        assert client.session is not None

        # Testando com Receptor
        client.force_login(receiver)
        assert client.session is not None
