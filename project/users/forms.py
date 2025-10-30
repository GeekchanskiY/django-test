from django import forms


class UploadAvatarForm(forms.Form):
    image = forms.ImageField(allow_empty_file=False, required=True)