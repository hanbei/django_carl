from __future__ import print_function

import csv

from django.core.management.base import BaseCommand
from recipes.models import Recipe


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file', nargs=1, type=str)

    def handle(self, *args, **options):
        f = options['file'][0]
        with open(f, 'rb') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                recipe = Recipe(title=row[1], description=row[2])
                recipe.save()
