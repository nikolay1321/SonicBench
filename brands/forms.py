from django import forms
from .models import Brand

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand

        fields = [
            "name",
            "country",
            "description",
            "website",
            "logo_url",
        ]

        labels = {
            "name": "Brand Name",
            "country": "Country of Origin",
            "description": "About the Brand",
            "website": "official Website",
            "logo_url": "Brand Logo URL",
        }

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "e.g. JBL",
            }),

            "country": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "e.g. United States",
            }),

            "description": forms.Textarea(attrs={
                "class": "form-input",
                "placeholder": "Tell us about this manufacturer...",
                "rows": 5,
            }),

            "website": forms.URLInput(attrs={
                "class": "form-input",
                "placeholder": "https://example.com",
            }),

            "logo_url": forms.URLInput(attrs={
                "class": "form-input",
                "placeholder": "https://example.com/logo.png",
            }),
        }

        help_texts = {
            "name": "Enter the manufacturer's name.",
            "website": "Include https:// at the beginning.",
            "logo_url": "Optional: enter a direct image URL.",
        }

        error_messages = {
            "name": {
                "required": "Please enter a brand name.",
                "unique": "A brand with this name already exists.",
            },

            "country":{
                "required": "Please enter the country of origin.",
            },

            "website": {
                "invalid": "Please enter a valid URL.",
            },

            "logo_url": {
                "invalid": "Please enter a valid image URL.",
            },
        }

    def clean_name(self):
        name = self.cleaned_data["name"].strip()

        existing_brands = Brand.objects.filter(
            name__iexact=name
        )

        if self.instance.pk:
            existing_brands = existing_brands.exclude(
                pk=self.instance.pk
            )

        if existing_brands.exists():
            raise forms.ValidationError(
                "This brand already exists in the catalog."
            )

        return name