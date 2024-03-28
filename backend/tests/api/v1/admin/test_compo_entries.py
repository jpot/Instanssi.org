import pytest

BASE_URL = "/api/v1/admin/compo_entries/"


@pytest.mark.django_db
@pytest.mark.parametrize(
    "method,status",
    [
        ("GET", 401),
        ("POST", 401),
        ("DELETE", 401),
        ("PATCH", 401),
        ("PUT", 401),
        ("HEAD", 401),
        ("OPTIONS", 401),
    ],
)
def test_unauthenticated_admin_compo_entries(api_client, method, status):
    assert api_client.generic(method, BASE_URL).status_code == status


@pytest.mark.django_db
@pytest.mark.parametrize(
    "method,status",
    [
        ("GET", 403),
        ("POST", 403),
        ("DELETE", 403),
        ("PATCH", 403),
        ("PUT", 403),
        ("HEAD", 403),
        ("OPTIONS", 403),
    ],
)
def test_unauthorized_admin_compo_entries(user_api_client, method, status):
    assert user_api_client.generic(method, BASE_URL).status_code == status


@pytest.mark.django_db
@pytest.mark.parametrize(
    "method,status",
    [
        ("GET", 200),
        ("POST", 403),
        ("DELETE", 403),
        ("PATCH", 403),
        ("PUT", 403),
        ("HEAD", 200),
        ("OPTIONS", 200),
    ],
)
def test_authenticated_admin_compo_entries(staff_api_client, method, status):
    assert staff_api_client.generic(method, BASE_URL).status_code == status
