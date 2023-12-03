from django.core.management import BaseCommand, call_command
from django.db import IntegrityError, ProgrammingError
from django.conf import settings

class Command(BaseCommand):

    def handle(self, *args, **options) -> None:
        fixtures_path = settings.BASE_DIR.joinpath('data.json')
        try:
            call_command('loaddata', fixtures_path)
        except ProgrammingError:
            pass
        except IntegrityError as e:
            self.stdout.write(f'Invalid Fixtures: {e}', self.style.NOTICE)
        else:
            self.stdout.write(
                'Command have been completed successfully', self.style.SUCCES
            )