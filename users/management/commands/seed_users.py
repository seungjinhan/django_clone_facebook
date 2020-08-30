from django.core.management.base import BaseCommand
from users.models import User, Hobby
from home.models import Photo
from django_seed import Seed
from django.contrib.admin.utils import flatten
import random


class Command(BaseCommand):

    help = 'this command creates users'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number', default=2, type=int, help='how many users do you want to create')

    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {
            'is_staff': False,
            "is_superuser": False,
            'is_active': True,
        })

        users = seeder.execute()
        users_keys = flatten(list(users.values()))

        hobbies = Hobby.objects.all()

        for pk in users_keys:
            user = User.objects.get(pk=pk)
            for a in hobbies:
                num = random.randint(0, 15)
                if num > 13:
                    user.hobbies.add(a)

        self.stdout.write(self.style.SUCCESS("Users created!"))
