from django.core.management.base import BaseCommand
from users.models import User
from home.models import Photo, Post
from django_seed import Seed
from django.contrib.admin.utils import flatten
import random


class Command(BaseCommand):

    help = 'this command creates post'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number', default=2, type=int, help='how many post do you want to create')

    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        users = User.objects.all()

        seeder.add_entity(Post, number, {
            'user': lambda x: random.choice(users)
        })

        seeder.execute()

        self.stdout.write(self.style.SUCCESS("Users created!"))
