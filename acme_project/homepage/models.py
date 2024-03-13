from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.
class BaseModel(models.Model):
    title_ru = models.CharField(
        max_length=256,
        null=False,
        blank=False,
        unique=True,
        verbose_name='Название'
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    modified_at = models.DateTimeField(
        auto_now_add=False,
        auto_now=True,
        verbose_name='Дата изменения'
    )

    class Meta:
        abstract = True


class GeoCategory(BaseModel):
    title_eng = models.CharField(
        max_length=256,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Тип территории'
        verbose_name_plural = 'Типы территорий'

    def __str__(self):
        return self.title_ru


class DistrictName(BaseModel):
    short_ru = models.CharField(
        max_length=12,
        null=False,
        blank=False,
    )

    title_eng = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Округ'
        verbose_name_plural = 'Округа'
        ordering = ('id',)

    def __str__(self):
        return self.short_ru


class TerritorialUnit(BaseModel):
    title_eng = models.CharField(
        max_length=256,
        unique=True,
        null=True,
        blank=True,
    )

    geo_category = models.ForeignKey(
        GeoCategory,
        on_delete=models.CASCADE,
        related_name='geo_category',
        verbose_name='Тип территории'
    )

    district = models.ForeignKey(
        DistrictName,
        on_delete=models.CASCADE,
        related_name='district',
        verbose_name='Округ',
        null=True
    )

    class Meta:
        verbose_name = 'Территориальная единица'
        verbose_name_plural = 'Территориальные единицы'

    def __str__(self):
        return self.title_ru


class Contingents(BaseModel):
    age = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(122)],
        blank=True,
        null=True,
        verbose_name='Возраст'
    )
    sex = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name='Пол'
    )

    class Meta:
        verbose_name = 'Контингент'
        verbose_name_plural = 'Контингенты'

    def __str__(self):
        return self.title_ru


class Units(BaseModel):
    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'

    def __str__(self):
        return self.title_ru


class ResidencePlace(BaseModel):
    title_eng = models.CharField(
        max_length=256,
        unique=True,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title_ru


class StatForm(models.Model):
    title_ru = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        unique=False,
        verbose_name='Название'
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание'
    )

    num_form = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='Номер формы',

    )

    count_table = models.PositiveSmallIntegerField(
        verbose_name='Кол-во таблиц',
        null=True,
    )

    class Meta:
        verbose_name = 'Отчетная форма'
        verbose_name_plural = 'Отчетные формы'

    def __str__(self):
        return self.num_form


class TableForm(models.Model):
    title_ru = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        unique=True,
        verbose_name='Название'
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание'
    )

    table_number = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name='Номер таблицы'
    )

    form = models.ForeignKey(
        StatForm,
        on_delete=models.CASCADE,
        verbose_name='Номер формы',
    )

    class Meta:
        unique_together = ('table_number', 'form')
        verbose_name = 'Таблицы форм'
        verbose_name_plural = 'Таблицы форм'

    def __str__(self):
        return self.title_ru


class PeriodMonth(BaseModel):
    class Meta:
        verbose_name = 'Месяц'
        verbose_name_plural = 'Месяцы'

    def __str__(self):
        return self.title_ru


class PeriodYear(BaseModel):
    class Meta:
        verbose_name = 'Год'
        verbose_name_plural = 'Года'

    def __str__(self):
        return self.title_ru


class NameOfDiseases(BaseModel):
    short_name = models.CharField(
        max_length=128,
        verbose_name='Сокр. название'
    )

    table_number = models.ForeignKey(
        TableForm,
        on_delete=models.CASCADE,
        verbose_name='Название таблицы'
    )

    first_name = models.BooleanField(
        verbose_name='Форма №1'
    )
    second_name = models.BooleanField(
        verbose_name='Форма №2'
    )

    class Meta:
        verbose_name = 'Название нозологии'
        verbose_name_plural = 'Список нозологий'

    def __str__(self):
        return self.short_name
