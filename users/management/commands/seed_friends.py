from django.core.management.base import BaseCommand
from users.models import User, Friends
from django_seed import Seed
from django.contrib.admin.utils import flatten
import random


class Command(BaseCommand):

    help = 'this command creates users'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number', default=2, type=int, help='how many users do you want to create')

    def handle(self, *args, **options):
        users = User.objects.all()

        for u in users:

            if random.randint(0, 2) % 2 == 0:

                f = Friends.objects.create(
                    is_block=True,
                    me=u
                )
                for u2 in users:
                    num = random.randint(0, 10)
                    if num > 9:
                        f.friend.add(u2)

        self.stdout.write(self.style.SUCCESS("Friends created!"))
