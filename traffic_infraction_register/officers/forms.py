from django import forms
from django.contrib.auth.models import User
from .models import Officer
from django.utils.translation import gettext_lazy as _



class OfficerForm(forms.ModelForm):
    first_name = forms.CharField(label=_("First Name"), max_length="50", required=True)
    last_name = forms.CharField(label=_("Last Name"), max_length="50", required=True)

    class Meta:
        model = Officer
        fields = ["badge", "password"]

    def __init__(self, *args, **kwargs):
        super(OfficerForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields["first_name"].initial = self.instance.user.first_name
            self.fields["last_name"].initial = self.instance.user.last_name

    def save(self, commit=True):
        user = User(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            username=self.cleaned_data['badge']
        )
        if commit:
            user.save()

        officer = super().save(commit=False)
        officer.user = user
        if commit:
            officer.save()
        return officer