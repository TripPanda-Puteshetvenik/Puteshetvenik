"""
Initial data fixture — run with:
  python manage.py loaddata initial_data
Or use the management command:
  python manage.py setup_initial_data
"""
from django.core.management.base import BaseCommand
from categories.models import Continent, Country, TravelType


CONTINENTS = [
    ('Европа', 'evropa', '🌍'),
    ('Азия', 'aziya', '🌏'),
    ('Америка', 'amerika', '🌎'),
    ('Африка', 'afrika', '🌍'),
    ('Австралия и Океания', 'avstraliya', '🌏'),
]

COUNTRIES = [
    # Европа
    ('Франция', 'frantsiya', 'evropa', '🇫🇷'),
    ('Италия', 'italiya', 'evropa', '🇮🇹'),
    ('Испания', 'ispaniya', 'evropa', '🇪🇸'),
    ('Гърция', 'gartsiya', 'evropa', '🇬🇷'),
    ('Германия', 'germaniya', 'evropa', '🇩🇪'),
    ('България', 'balgariya', 'evropa', '🇧🇬'),
    ('Португалия', 'portugaliya', 'evropa', '🇵🇹'),
    ('Хърватия', 'harvatiya', 'evropa', '🇭🇷'),
    ('Нидерландия', 'niderlandiya', 'evropa', '🇳🇱'),
    ('Австрия', 'avstriya', 'evropa', '🇦🇹'),
    # Азия
    ('Япония', 'yaponiya', 'aziya', '🇯🇵'),
    ('Тайланд', 'tayland', 'aziya', '🇹🇭'),
    ('Виетнам', 'vietnam', 'aziya', '🇻🇳'),
    ('Индия', 'indiya', 'aziya', '🇮🇳'),
    ('Индонезия', 'indoneziya', 'aziya', '🇮🇩'),
    # Америка
    ('САЩ', 'sashт', 'amerika', '🇺🇸'),
    ('Мексико', 'meksiko', 'amerika', '🇲🇽'),
    ('Бразилия', 'braziliya', 'amerika', '🇧🇷'),
    ('Аржентина', 'arzentina', 'amerika', '🇦🇷'),
    ('Перу', 'peru', 'amerika', '🇵🇪'),
    # Африка
    ('Мароко', 'maroko', 'afrika', '🇲🇦'),
    ('Кения', 'keniya', 'afrika', '🇰🇪'),
    ('ЮАР', 'yuar', 'afrika', '🇿🇦'),
    ('Египет', 'egipet', 'afrika', '🇪🇬'),
    # Австралия
    ('Австралия', 'avstraliya-strana', 'avstraliya', '🇦🇺'),
    ('Нова Зеландия', 'nova-zelandiya', 'avstraliya', '🇳🇿'),
]

TRAVEL_TYPES = [
    ('extreme', '🧗'),
    ('family', '👨‍👩‍👧‍👦'),
    ('budget', '💰'),
    ('luxury', '✨'),
    ('adventure', '🏕️'),
    ('cultural', '🏛️'),
    ('beach', '🏖️'),
    ('mountain', '⛰️'),
]


class Command(BaseCommand):
    help = 'Setup initial categories data'

    def handle(self, *args, **kwargs):
        # Continents
        continent_map = {}
        for name, slug, icon in CONTINENTS:
            c, created = Continent.objects.get_or_create(slug=slug, defaults={'name': name, 'icon': icon})
            continent_map[slug] = c
            if created:
                self.stdout.write(f'  Created continent: {name}')

        # Countries
        for name, slug, cont_slug, flag in COUNTRIES:
            continent = continent_map.get(cont_slug)
            if continent:
                Country.objects.get_or_create(slug=slug, defaults={'name': name, 'continent': continent, 'flag': flag})

        # Travel types
        for name, icon in TRAVEL_TYPES:
            TravelType.objects.get_or_create(name=name, defaults={'icon': icon})

        self.stdout.write(self.style.SUCCESS('Initial data loaded successfully!'))
