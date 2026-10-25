from django.db import models
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator

# Create your models here.

class Speaker(models.Model):
    class SpeakerType(models.TextChoices):
        BOOKSHELF = "bookshelf", "Bookshelf"
        FLOORSTANDING = "floorstanding", "Floorstanding"
        PORTABLE = "portable", "Portable"
        STUDIO_MONITOR = "studio_monitor", "Studio Monitor"
        SUBWOOFER = "subwoofer", "Subwoofer"

    brand = models.ForeignKey(
        "brands.Brand",
        on_delete=models.PROTECT,
        related_name="speakers",
    )

    name = models.CharField(
        max_length=120,
        validators=[
            MinLengthValidator(3),
        ],
    )

    speaker_type = models.CharField(
        max_length=20,
        choices=SpeakerType.choices,
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        validators=[
            MinValueValidator(Decimal("0.01")),
        ],
    )

    power_rms = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
        ],
    )

    frequency_min = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
        ],
    )

    frequency_max = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
        ],
    )

    is_wireless = models.BooleanField(
        default=False,
    )

    image_url = models.URLField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def clean(self):
        super().clean()

        if(
            self.frequency_min is not None
            and self.frequency_max is not None
            and self.frequency_max <= self.frequency_min
        ):
            raise ValidationError({
                "frequency_max": (
                    "Maximum frequency must be greater than minimum frequency."
                )
            })

    def __str__(self):
        return f"{self.brand} {self.name}"

    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["brand", "name"],
                name="unique_speaker_per_brand",
            )
        ]