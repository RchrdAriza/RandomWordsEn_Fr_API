from django.core.management.base import BaseCommand
from en.models import EnLangWord


class Command(BaseCommand):
    help = "Load words into the database"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to text file')

    def handle(self, *args, **options):
        file_path = options['file_path']
        with open(file_path, 'r') as file:
            for line in file:
                word = line.strip()
                EnLangWord.objects.create(word=word)
            self.stdout.write(self.style.SUCCESS("Words successfully loaded"))
