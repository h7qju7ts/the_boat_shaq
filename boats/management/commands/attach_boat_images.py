from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from boats.models import Boat


class Command(BaseCommand):
    help = "Attach existing images in media/boats to boats based on slug"

    def handle(self, *args, **kwargs):
        media_path = Path(settings.MEDIA_ROOT) / "boats"
        updated = 0

        if not media_path.exists():
            self.stdout.write(self.style.ERROR(f"Folder not found: {media_path}"))
            return

        for boat in Boat.objects.all():
            for ext in [".webp", ".jpg", ".jpeg", ".png"]:
                image_file = media_path / f"{boat.slug}{ext}"

                if image_file.exists():
                    boat.image.name = f"boats/{boat.slug}{ext}"
                    boat.save(update_fields=["image"])
                    updated += 1
                    self.stdout.write(f"Attached: {boat.slug}")
                    break

        self.stdout.write(self.style.SUCCESS(f"Total attached: {updated}"))