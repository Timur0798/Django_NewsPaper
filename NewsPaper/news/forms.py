from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'newsCategory','title','text']

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("title")
        name = cleaned_data.get("text")

        if name == description:
            raise ValidationError(
                "Описание не должно быть идентично содержанию публикации."
            )

        return cleaned_data