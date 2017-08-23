from django.core.management.base import BaseCommand, CommandError
from shortener.models import KirrURL

class Command(BaseCommand):
    help = "Refreshes all KirrURL shortcodes"

    def add_arguments(self,parser):
        parser.add_argument('--items',type = int)  #the -- signifies that we can run refreshcodes without pasiing any arguments

    def handle(self, *args,**options):
        return KirrURL.objects.refresh_shortcode(items = options['items'])  
