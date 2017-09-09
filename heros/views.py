import logging
import collections

from django.shortcuts import render
from django.views.decorators.http import require_GET

from heros.models import Hero


LOGGER = logging.getLogger(__name__)


@require_GET
def heros(request):
    """
    Main homepage view.
    """
    heros_data = collections.OrderedDict()
    for category, category_name in Hero.HERO_CATEGORY_CHOICES:
        heros_data.update(
            {
                category: {
                    'name': category_name,
                    'heros': Hero.objects.filter(category=category),
                }
            }
        )
    context = {
        'heros_data': heros_data
    }
    return render(request, 'heros.html', context)
