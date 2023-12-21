from django import forms
from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'name', 'description', 'preview', 'price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, fild in self.fields.items():
            fild.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        ban_words = ['крипта', 'казино', 'криптовалюта', 'биржа', 'дешево', 'бесплатно', 'радар', 'полиция', 'обман']

        for word in ban_words:
            if word in cleaned_data:
                raise forms.ValidationError('Данное наименование находится в списке запрещенных слов')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        ban_words = ['крипта', 'казино', 'криптовалюта', 'биржа', 'дешево', 'бесплатно', 'радар', 'полиция', 'обман']

        for word in ban_words:
            if word in cleaned_data:
                raise forms.ValidationError('Данное описание находится в списке запрещенных слов')
        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, fild in self.fields.items():
            if field_name != 'activate':
                fild.widget.attrs['class'] = 'form-control'
