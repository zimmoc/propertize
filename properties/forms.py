from django import forms
from properties.models import PropertyNotice

class PropertyNoticeForm(forms.ModelForm):
    class Meta:
        model = PropertyNotice
        fields = ['title', 'body', 'property', 'posted_by']
        css = {"all": ["form-control form-control-user"]}

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields['property'].queryset = user.properties.all()
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})