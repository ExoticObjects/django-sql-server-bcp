import datetime
from random import random
from django_sql_server_bcp import BCP
from django.core.management.base import BaseCommand
from main.models import StockPrice

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--rows', type=int, dest='row_count', default=500)

    def handle(self, row_count, **options):
        rows = []
        for _ in range(1, row_count):
            rows.append(dict(
                symbol='GOOG',
                price='%.2f' % (1000 * random()),
                timestamp=str(datetime.datetime.now())
            ))

        bcp = BCP(StockPrice)
        bcp.save(rows)
