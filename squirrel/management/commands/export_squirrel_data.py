from django.core.management.base import BaseCommand
from squirrel.models import Squirrel
import csv

class Command(BaseCommand):
    help = 'Command to export the squirrel database to .csv file. The first argument should be the path to file'

    def add_arguments(self, parser):
        parser.add_argument('args', type=str, nargs='*')

    def handle(self, *args, **kwargs):
        path = args[0]
        fields = Squirrel._meta.fields
        field_names = [field.name for field in fields]
        with open(path, 'w') as f:
            writer = csv.writer(f)
            for i in Squirrel.objects.all():
                #row = [getattr(i, field.name) for field in fields]
                writer.writerow([getattr(i, field) for field in field_names])
            f.close()

