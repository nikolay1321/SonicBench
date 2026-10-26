from django import forms

from .models import Speaker

class SpeakerForm(forms.ModelForm):
    class Meta:
        model = Speaker

        fields = [
            "brand",
            "name",
            "speaker_type",
            "description",
            "price",
            "power_rms",
            "frequency_min",
            "frequency_max",
            "is_wireless",
            "image_url",
        ]

        labels = {
            "brand": "Manufacturer",
            "name": "Speaker Model",
            "speaker_type": "Speaker Category",
            "description": "Description",
            "price": "Price",
            "power_rms": "RMS Power (W)",
            "frequency_min": "Minimum Frequency (Hz)",
            "frequency_max": "Maximum Frequency (Hz)",
            "is_wireless": "Wireless Speaker",
            "image_url": "Speaker Image URL",
        }

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "e.g. Studio Monitor 100",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-input",
                "rows": 5,
                "placeholder": "Describe the speaker...",
            }),
            "price": forms.NumberInput(attrs={
                "class": "form-input",
                "step": "0.01",
            }),
            "power_rms": forms.NumberInput(attrs={
                "class": "form-input",
            }),
            "frequency_min": forms.NumberInput(attrs={
                "class": "form-input",
            }),
            "frequency_max": forms.NumberInput(attrs={
                "class": "form-input",
            }),
            "image_url": forms.URLInput(attrs={
                "class": "form-input",
                "placeholder": "https://example.com/speaker.jpg",
            }),
        }

    def clean(self):
        cleaned_data = super().clean()

        minimum = cleaned_data. get("frequency_min")
        maximum = cleaned_data.get("frequency_max")

        if (
            minimum is not None and maximum is not None and maximum <= minimum
        ):
            self.add_error(
                "frequency_max",
                "Maximum frequency must be greater than minimum frequency.",
            )

        return cleaned_data

class SpeakerEditForm(SpeakerForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["brand"].disabled = True