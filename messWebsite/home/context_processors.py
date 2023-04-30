from .models import Caterer
'''
File-name: context_processors.py
Functions: base
Used to send All Caterers Information as context in the base template
'''
def base(request):
    return {'all_caterer' : Caterer.objects.all()}