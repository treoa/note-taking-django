from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import Content


class BaseViewForm(forms.ModelForm):
    title=forms.CharField(
        max_length=152,
        required=False,
    )
    image=forms.ImageField(
        required=False,
    )
    audio=forms.FileField(
        required=False,
    )

    class Meta:
        model=Content
        fields=['title', 'date_created', 'my_content', 'image', 'audio']

    def clean(self):
        deleted_data=super(BaseView, self).clean()

        item_1=deleted_data.get('title')
        item_2=deleted_data.get('content')

        if item_1 is not None and item_2 is not None:
            if len(item_2) < 8:
                self.add_error('content', ValidationError('The message is too short'))


class UpdateViewForm(forms.ModelForm):
    title=forms.CharField(
        max_length=152,
        required=False
    )
    image=forms.ImageField(
        required=False
    )
    image_clear=forms.BooleanField(
        required=False,
    )
    audio=forms.FileField(
        required=False
    )
    audio_clear=forms.FileField(
        required=False,
    )

    class Meta:
        model=Content
        fields=['title', 'date_created', 'my_content', 'image', 'audio']

    def clear(self):
        deleted_data=super(UpdateView, self).clean()

        item_1=deleted_data.get('title')
        item_2=deleted_data.get('date_created')
        item_3=deleted_data.get('content')

        if item_1 is not None and item_3 is not None:
            if len(item_3) < 8:
                self.add_error('content', ValidationError('The message is too short'))
