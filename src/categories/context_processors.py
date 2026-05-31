from .models import Continent, TravelType


def categories_context(request):
    return {
        'continents': Continent.objects.all(),
        'travel_types': TravelType.objects.all(),
    }
