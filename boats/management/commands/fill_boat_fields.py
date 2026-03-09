from django.core.management.base import BaseCommand
from faker import Faker
import random

from boats.models import Boat, Brand, Category

fake = Faker()


class Command(BaseCommand):
    help = "Fill missing boat fields while keeping existing images"

    def handle(self, *args, **kwargs):
        brands = ["Yamaha", "Bayliner", "Sea Ray", "Sunseeker", "Beneteau", "Tracker", "Boston Whaler"]

        brand_objs = []
        for name in brands:
            brand_objs.append(Brand.objects.get_or_create(name=name)[0])

        boats = Boat.objects.select_related("category", "brand").all()

        updated_count = 0

        for boat in boats:
            changed = False

            if not boat.brand:
                boat.brand = random.choice(brand_objs)
                changed = True

            if not boat.short_description:
                boat.short_description = fake.sentence(nb_words=10)
                changed = True

            if not boat.description:
                boat.description = fake.paragraph(nb_sentences=5)
                changed = True

            if not boat.price:
                boat.price = random.randint(5000, 120000)
                changed = True

            if not boat.length_ft:
                boat.length_ft = round(random.uniform(12, 40), 2)
                changed = True

            if not boat.year:
                boat.year = random.randint(2005, 2024)
                changed = True

            # Keep existing image untouched
            # Do not assign anything to boat.image

            if changed:
                boat.save()
                updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(f"Updated {updated_count} boats while keeping images.")
        )