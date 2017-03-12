from django import forms

from .models import blog,comment

class blogform(forms.ModelForm):

    class Meta:
        model = blog
        fields = ('title','body','date')


class comentform(forms.ModelForm):

    class Meta:
        model = comment
        fields = ('blog','comment', 'date')
