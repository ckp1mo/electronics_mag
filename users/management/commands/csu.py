from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        admin = User.objects.create(
            username='admin',
            is_active=True,
            is_superuser=True,
            is_staff=True
        )
        admin.set_password('qwerty')
        admin.save()
