from django import forms
from .models import FirstForm
from pprint import pprint


class FirstChoiceForm(forms.Form):
    territory_choices = (
        FirstForm.objects.values_list('territory__id', 'territory__title_ru',
                                      ).order_by('territory__id').distinct()
    )

    years_choices = (
        FirstForm.objects.values_list('period_year__title_ru',
                                      'period_year__title_ru',
                                      ).order_by('period_year__id').distinct()
    )

    months_choices = (
        (1, 'Январь'),
        (2, 'Февраль'),
        (3, 'Март'),
        (4, 'Апрель'),
        (5, 'Май'),
        (6, 'Июнь'),
        (7, 'Июль'),
        (8, 'Август'),
        (9, 'Сентябрь'),
        (10, 'Октябрь'),
        (11, 'Ноябрь'),
        (12, 'Декабрь'),
    )
    territory = forms.MultipleChoiceField(choices=territory_choices,
                                          widget=forms.CheckboxSelectMultiple)

    years = forms.MultipleChoiceField(choices=years_choices,
                                      widget=forms.CheckboxSelectMultiple)

    months = forms.MultipleChoiceField(choices=months_choices,
                                      widget=forms.CheckboxSelectMultiple)


