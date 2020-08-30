from django.core.management.base import BaseCommand
from users.models import Hobby


class Command(BaseCommand):

    help = 'this command creates amenities'

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         '--times', help='how many time do you want me to tell')

    def handle(self, *args, **options):
        hobbies = [
            "3D printing",
            "Acrobatics",
            "Acting",
            "Amateur radio",
            "Animation",
            "Aquascaping",
            "Astrology",
            "Astronomy",
            "Baking",
            "Baton twirling",
            "Blogging",
            "Building",
            "Board/tabletop games",
            "Book discussion clubs",
            "Book restoration",
            "Bowling",
            "Brazilian jiu-jitsu",
            "Breadmaking",
            "Bullet journaling",
            "Cabaret",
            "Calligraphy",
            "Candle making",
            "Candy making",
            "Car fixing & building",
            "Card games",
            "Cheesemaking",
            "Cleaning",
            "Clothesmaking",
            "Coffee roasting",
            "Collecting",
            "Coloring",
            "Computer programming",
            "Confectionery",
            "Cooking",
            "Cosplaying",
            "Couponing",
            "Craft",
            "Creative writing",
            "Crocheting",
            "Cross-stitch",
            "Crossword puzzles",
            "Cryptography",
            "Cue sports",
            "Dance",
        ]
        for a in hobbies:
            Hobby.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("hobbies created!"))
