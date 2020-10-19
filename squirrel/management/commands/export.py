import csv

from django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrels


class Command(BaseCommand):
    help = 'A command that can be used to export the data in CSV format'

    def add_arguments(self, parser):
        parser.add_argument('args', type=str, nargs='*')

    def handle(self, *args, **kwargs):
        path = args[0]
        fields = Squirrels._meta.fields
        with open(path, 'w') as f:
            writer = csv.writer(f)
            for i in Squirrels.objects.all():
                row = [getattr(i, field.name) for field in fields]
                writer.writerow(row)
            f.close()
