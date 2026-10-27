from decimal import Decimal

from django import forms

from .models import Room, ListeningSetup

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room

        fields = [
            'name',
            'room_type',
            'area_sqm',
            'description',
        ]

        labels = {
            'name': 'Room Name',
            'room_type': 'Room Type',
            'area_sqm': 'Room Area (m²)',
            'description': 'Room Description',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. My Living Room',
            }),

            'room_type': forms.Select(attrs={
                'class': 'form-input',
            }),

            'area_sqm': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. 25.50',
                'step': '0.01',
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Describe your listening room...',
                'rows': 4,
            }),
        }

        error_messages = {
            'name': {
                'required': 'Please enter a room name.',
            },

            'area_sqm': {
                'required': 'Please enter the room area.',
                'invalid': 'Please enter a valid number.'
            },
        }

    def clean_area_sqm(self):
        area = self.cleaned_data['area_sqm']

        if area > Decimal("1000.00"):
            raise forms.ValidationError("Room area cannot exceed 1000 square meters.")

        return area

class ListeningSetupForm(forms.ModelForm):
    class Meta:
        model = ListeningSetup

        fields = [
            'name',
            'room',
            'speakers',
            'purpose',
            'notes'
        ]

        labels = {
            'name': 'Setup Name',
            'room': 'Listening Room',
            'speakers': 'Speakers',
            'purpose': 'Setup Purpose',
            'notes': 'Additional Notes',
        }

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "e.g. My Home Audio System",
            }),

            "room": forms.Select(attrs={
                "class": "form-input",
            }),

            "speakers": forms.SelectMultiple(attrs={
                "class": "form-input",
                "size": 6,
            }),

            "purpose": forms.Select(attrs={
                "class": "form-input",
            }),

            "notes": forms.Textarea(attrs={
                "class": "form-input",
                "rows": 4,
                "placeholder": "Describe your sound setup...",
            }),
        }

        help_texts = {
            "speakers": (
                "Hold Ctrl to select multiple speakers on Windows."
            ),
        }

        error_messages = {
            "name": {
                "required": "Please enter a setup name.",
            },

            "room": {
                "required": "Please select a listening room.",
            },

            "speakers": {
                "required": "Please select at least one speaker.",
            },

            "purpose": {
                "required": "Please select a setup purpose.",
            },
        }