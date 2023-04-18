from .models import Caterer

def base(request):
    return {'all_caterer' : Caterer.objects.all()}