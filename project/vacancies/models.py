from django.db import models

class Employer(models.Model):
    name = models.CharField(max_length=255, verbose_name='работодатель')

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    name = models.CharField(max_length=255, verbose_name='вакансия')
    salary = models.IntegerField(verbose_name='заработная плата')
    employer = models.ForeignKey(to=Employer, on_delete=models.CASCADE, verbose_name='работодатель')

    class Meta:
        verbose_name='вакансия'
        verbose_name_plural='вакансии'

    def __str__(self):
        return self.name
