from django.db import models
from decimal import Decimal
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

# Create your models here.

class Room(models.Model):
    class RoomType(models.TextChoices):
        BEDROOM = "bedroom", "Bedroom"
        LIVING_ROOM = "living_room", "Living Room"
        HOME_THEATER = "home_theater", "Home Theater"
        STUDIO = "studio", "Recording Studio"
        OFFICE = "office", "Office"

    name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(3),
        ],
    )

    room_type = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[
            MinValueValidator(Decimal("1.00")),
        ],
    )

    description = models.TextField(
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

class ListeningSetup(models.Model):
        class SetupPurpose(models.TextChoices):
            MUSIC = "music", "Music Listening"
            HOME_THEATER = "home_theater", "Home Theater"
            GAMING = "gaming", "Gaming"
            STUDIO = "studio", "Studio Monitoring"

        name = models.CharField(
            max_length=120,
            validators=[
                MinLengthValidator(3),
            ],
        )

        room = models.ForeignKey(
            Room,
            on_delete=models.PROTECT,
            related_name="listening_setups",
        )

        speakers = models.ManyToManyField(
            "speakers.Speaker",
            related_name="listening_setups",
            blank=False,
        )

        purpose = models.CharField(
            max_length=20,
            choices=SetupPurpose.choices,
        )

        notes = models.TextField(
            blank=True,
        )

        created_at = models.DateTimeField(
            auto_now_add=True,
        )

        def __str__(self):
            return self.name

        class Meta:
            ordering = ["-created_at"]
