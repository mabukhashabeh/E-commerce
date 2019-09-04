from django import forms
from django.utils.translation import ugettext_lazy as _



class SearchItemForm(forms.Form):
    item = forms.CharField(
        label=False,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': _('Search Item'), 'autocomplete': 'off' }))
