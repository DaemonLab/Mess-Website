from .models import Caterer
'''
File-name: context_processors.py
Functions: base
Used to send All Caterers Information as context in the base template
'''
def base(request):
    caterer = Caterer.objects.filter(visible=True).all()
    return {'all_caterer' : caterer}