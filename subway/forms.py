from cProfile import label
from email.policy import default

from crispy_forms_foundation.layout import Fieldset
from django import forms
from django.contrib.admin.helpers import Fieldline
from django.contrib.postgres.fields.utils import AttributeSetter

from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import InlineField
from crispy_forms.layout import Layout, Field, MultiField


class CountForm(forms.ModelForm):

    vendre_adjuste = forms.FloatField(label=_("Vendre ajusté"), min_value=0.0, max_value=10000.0)
    vendre_par_cardre = forms.FloatField(label=_("Vendre par carte"), min_value=0.0, max_value=10000.0)
    depot = forms.FloatField(label=_("Dépôt"), min_value=0.0, max_value=10000.0)

    five_cent = forms.IntegerField(label=_('5¢'), min_value=0, max_value=1000)
    ten_cent = forms.IntegerField(label=_('10¢'), min_value=0, max_value=1000)
    twenty_five_cent = forms.IntegerField(label=_('25¢'), min_value=0, max_value=1000)
    one_dollar = forms.IntegerField(label=_('1$'), min_value=0, max_value=1000)
    two_dollar = forms.IntegerField(label=_('2$'), min_value=0, max_value=1000)
    five_dollar = forms.IntegerField(label=_('5$'), min_value=0, max_value=1000)
    ten_dollar = forms.IntegerField(label=_('10$'), min_value=0, max_value=1000)
    twenty_dollar = forms.IntegerField(label=_('20$'), min_value=0, max_value=1000)
    fifty_dollar = forms.IntegerField(label=_('50$'), min_value=0, max_value=1000)
    hundred_dollar = forms.IntegerField(label=_('100$'), min_value=0, max_value=1000)

    class Meta:
        pass


    field_order = ['vendre_adjuste', 'vendre_par_cardre', 'depot', 'five_cent', 'ten_cent', 'twenty_five_cent',
                   'one_dollar', 'two_dollar',
                   'five_dollar', 'ten_dollar',
                   'twenty_dollar', 'fifty_dollar', 'hundred_dollar']
