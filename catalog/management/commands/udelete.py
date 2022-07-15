from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class Command(BaseCommand):
    help = 'Delete user with current id'

    def add_arguments(self, parser):
        parser.add_argument('id', nargs='+', type=int,
                            help='which user will be deleted(id of the user)')

    def handle(self, *args, **options):
        users_id = options['id']
        for pk in users_id:
            try:
                acc = User.objects.get(pk=pk)
                if acc.is_superuser:
                    self.stdout.write(
                        self.style.WARNING('You cant delete a superuser\n'))
                else:
                    acc.delete()
                    self.stdout.write(
                        self.style.SUCCESS(f'User with id {pk} was successfully deleted\n'))
            except ObjectDoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f'No user with this id {pk}\n'))
