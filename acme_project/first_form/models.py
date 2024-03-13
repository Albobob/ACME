from django.db import models
from django.core.validators import MinValueValidator, ValidationError
from homepage.models import TerritorialUnit, NameOfDiseases, Contingents
from homepage.models import Units, PeriodMonth, PeriodYear


# Create your models here.
class FirstForm(models.Model):
    territory = models.ForeignKey(
        TerritorialUnit,
        on_delete=models.CASCADE,
        verbose_name='Территория',
    )

    name_of_diseases = models.ForeignKey(
        NameOfDiseases,
        on_delete=models.CASCADE,
        verbose_name='Нозология'
    )

    # Возрастная группа в популяции
    contingents = models.ForeignKey(
        Contingents,
        on_delete=models.CASCADE,
        verbose_name='Контингент/Возрастная группа',
    )

    unit = models.ForeignKey(
        Units,
        on_delete=models.CASCADE,
        verbose_name='Единица измерения'
    )

    period_month = models.ForeignKey(
        PeriodMonth,
        on_delete=models.CASCADE,
        verbose_name='Месяц'
    )

    period_year = models.ForeignKey(
        PeriodYear,
        on_delete=models.CASCADE,
        verbose_name='Год'
    )

    value = models.FloatField(
        null=False,
        blank=False,
        validators=[MinValueValidator(0)],
        verbose_name='Значение'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения'
    )

    class Meta:
        unique_together = (
            'territory', 'name_of_diseases', 'contingents', 'unit',
            'period_month', 'period_year')


        verbose_name = 'Форма №1'
        verbose_name_plural = 'Форма №1'
