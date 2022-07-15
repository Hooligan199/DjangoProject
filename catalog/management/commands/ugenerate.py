import random
import string
from faker import Faker
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Generate from 1 to 10 users(only)'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int,
                            help='how many users will be created(from 1-10)')

    def handle(self, *args, **options):
        number = options['number']
        fake = Faker()
        if 1 <= number <= 10:
            for _ in range(number):
                User.objects.create_user(
                    fake.name(),
                    rand_email(),
                    User.objects.make_random_password()
                )
            self.stdout.write(self.style.SUCCESS(f'{number} users created\n'))
        else:
            raise CommandError(self.stdout.write(self.style.ERROR('Wrong argument')))


def rand_email():
    letters = list(string.ascii_lowercase[:26])
    s = ''
    for i in range(4):
        s = s+letters[random.randint(0, 25)]
    for k in range(3):
        n = random.randint(0, 9)
        s = s+str(n)
    return s + "@gmail.com"
