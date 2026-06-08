from .models import Caterer, GlobalConstants

"""
File-name: context_processors.py
Functions: base
Used to send All Caterers Information as context in the base template
"""


def base(request):
    caterer = Caterer.objects.filter(visible=True).all()
    constants = GlobalConstants.objects.first()
    if not constants:
        # Provide defaults if no constants exist yet
        constants = GlobalConstants.objects.create()
    return {"all_caterer": caterer, "constants": constants}
