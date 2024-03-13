from django.db import models
from django.core.validators import MinValueValidator, ValidationError
from homepage.models import TerritorialUnit, StatForm, NameOfDiseases


class Smp(models.Model):
    territorial_unit = models.ForeignKey(
        TerritorialUnit,
        on_delete=models.CASCADE,
        related_name='smp_territorial_unit',
        verbose_name='Регион',
    )

    value = models.FloatField(
        verbose_name='СМП',
        null=False,
        blank=False,
        validators=[MinValueValidator(0)]
    )

    form = models.ForeignKey(
        StatForm,
        on_delete=models.CASCADE,
        related_name='smp_form',
        verbose_name='Номер формы'
    )

    name_of_diseases = models.ForeignKey(
        NameOfDiseases,
        on_delete=models.CASCADE,
        related_name='smp_nod',
        verbose_name='Нозология'
    )

    from_to_year = models.CharField(
        max_length=10,
        verbose_name='Период расчета (пример: 2010_2022)'
    )

    from_year = models.DateField(
        verbose_name='Начальная дата'
    )

    to_year = models.DateField(
        verbose_name='Конечная дата'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения'
    )

    def clean(self):
        if self.from_year.month != self.to_year.month:
            raise ValidationError(
                'Месяц начальной даты не совпадает с месяцем конечной даты')

    class Meta:
        verbose_name = 'СМП'
        verbose_name_plural = 'СМП'
