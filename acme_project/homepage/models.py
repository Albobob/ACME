from django.db import models


# Create your models here.
class BaseModel(models.Model):
    title_ru = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        unique=True,
        verbose_name='Название'
    )

    description = models.TextField(
        null=True,
        blank=False,
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
    age = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='Возраст'
    )
    sex = models.CharField(
        max_length=256,
        blank=False,
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

