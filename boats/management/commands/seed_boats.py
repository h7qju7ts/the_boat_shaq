from django.core.management.base import BaseCommand
from faker import Faker
import random

from boats.models import Boat, Brand, Category

fake = Faker()


class Command(BaseCommand):
    help = "Generate sample boat data"

    def handle(self, *args, **kwargs):

        brands = ["Yamaha", "Bayliner", "Sea Ray", "Sunseeker", "Beneteau"]
        categories = ["Kayaks", "Fishing Boats", "Motorboats", "Sailboats", "Yachts"]

        brand_objs = []
        category_objs = []

        for b in brands:
            brand_objs.append(Brand.objects.get_or_create(name=b)[0])

        for c in categories:
            category_objs.append(Category.objects.get_or_create(name=c)[0])

        for i in range(20):

            name = f"{random.choice(brands)} {fake.word().title()}"

            Boat.objects.create(
                name=name,
                brand=random.choice(brand_objs),
                category=random.choice(category_objs),
                description=fake.paragraph(nb_sentences=5),
                short_description=fake.sentence(),
                price=random.randint(2000, 120000),
                length_ft=random.uniform(10, 45),
                year=random.randint(2000, 2024),
                is_available=True,
            )

        self.stdout.write(self.style.SUCCESS("Sample boats created!"))