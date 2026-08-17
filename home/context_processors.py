from django.core.cache import cache

from .models import Caterer, Contact, GlobalConstants

"""
File-name: context_processors.py
Functions: base
Used to send All Caterers Information as context in the base template
"""

FOOTER_CONTACT_CACHE_KEY = "footer_contact"
FOOTER_CONTACT_EMAIL = "gs.dining@iiti.ac.in"
FOOTER_CONTACT_CACHE_TIMEOUT = 60 * 60 * 24  # 1 day
_MISSING = object()


def get_footer_contact():
    cached = cache.get(FOOTER_CONTACT_CACHE_KEY, _MISSING)
    if cached is not _MISSING:
        return cached

    contact = (
        Contact.objects.filter(email__iexact=FOOTER_CONTACT_EMAIL)
        .only("name", "occupation", "email", "contact")
        .first()
    )
    data = (
        {
            "name": contact.name,
            "occupation": contact.occupation,
            "email": contact.email,
            "phone": contact.contact,
        }
        if contact
        else {}
    )
    cache.set(FOOTER_CONTACT_CACHE_KEY, data, FOOTER_CONTACT_CACHE_TIMEOUT)
    return data


def base(request):
    caterer = Caterer.objects.filter(visible=True).all()
    constants = GlobalConstants.objects.first()
    if not constants:
        # Provide defaults if no constants exist yet
        constants = GlobalConstants.objects.create()
    return {
        "all_caterer": caterer,
        "constants": constants,
        "footer_contact": get_footer_contact(),
    }
