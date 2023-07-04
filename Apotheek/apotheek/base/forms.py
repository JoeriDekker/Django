from django import forms
from .models import Medicine, Collection, Profile

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your Name", max_length=100)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("city", "bio", "date_of_birth")

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ("name", "manufacture", "cures", "side_effects")

class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ('medicine', 'user', 'date')