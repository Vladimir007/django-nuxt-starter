from .models import User


def example_task():
    return "Example task completed"


def test_task(user: User):
    return user.email
