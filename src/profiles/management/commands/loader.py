from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from home import utils as home_utils

User = get_user_model()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("count", nargs="?", default=10, type=int)
        parser.add_argument("--show-total", action="store_true", default=False)

    def handle(self, *args, **options):
        count = options.get("count")
        show_total = options.get("show_total")
        profiles = home_utils.get_fake_profiles(count=count)
        new_users = []
        for profile in profiles:
            new_users.append(User(**profile))
        user_bulk = User.objects.bulk_create(new_users, ignore_conflicts=True)
        print(f"New user ct: {len(user_bulk)}")
        if show_total:
            print(f"User.objects.count(): {User.objects.count()}")
