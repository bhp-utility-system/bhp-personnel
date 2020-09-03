from django import forms
from django.core.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidator, FormValidatorMixin

from ..models import Contract


class ContractFormValidator(FormValidator):

    def clean(self):
        super().clean()

        duration = self.cleaned_data.get('duration')
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')

        if duration == '2 Years':
            next_date = start_date + relativedelta(years=2)

            if next_date != end_date:
                message = {'duration':
                           'Contract duration must '
                           'match the contract end date'}
                self._errors.update(message)
                raise ValidationError(message)

        if duration == '1 Year':
            next_date = start_date + relativedelta(years=1)

            if next_date != end_date:
                message = {'duration':
                           'Contract duration must '
                           'match the contract end date'}
                self._errors.update(message)
                raise ValidationError(message)

        if duration == '6 Months':
            next_date = start_date + relativedelta(months=6)

            if next_date != end_date:
                message = {'duration':
                           'Contract duration must '
                           'match the contract end date'}
                self._errors.update(message)
                raise ValidationError(message)


class ContractForm(FormValidatorMixin, SiteModelFormMixin, forms.ModelForm):

    form_validator_cls = ContractFormValidator

    identifier = forms.CharField(
        label='Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Contract
        fields = '__all__'
