from django import forms
from django.contrib.auth.models import User
from .models import Officer
from django.utils.translation import gettext_lazy as _


class OfficerForm(forms.ModelForm):
    first_name = forms.CharField(label=_("First Name"), max_length="50", required=True)
    last_name = forms.CharField(label=_("Last Name"), max_length="50", required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = Officer
        fields = ["badge"]

    def __init__(self, *args, **kwargs):
        super(OfficerForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields["first_name"].initial = self.instance.user.first_name
            self.fields["last_name"].initial = self.instance.user.last_name
            self.fields["password"].initial = ""
        else:
            self.fields["password"].required = True

    def save(self, commit=True):
        user = user = self.instance.user if self.instance.pk else User()

        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.username = self.cleaned_data["badge"]

        if self.cleaned_data["password"]:
            user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

        officer = super().save(commit=False)
        officer.user = user
        if commit:
            officer.save()
        return officer
