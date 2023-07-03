from django import forms
from .models import Medicine, Collection

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your Name", max_length=100)

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ("name", "manufacture", "cures", "side_effects")

class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ("medicine", "date")