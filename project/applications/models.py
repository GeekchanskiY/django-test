from django.db import models
from django.conf import settings


class Application(models.Model):
    want_salary = models.IntegerField(verbose_name='желаемая зп')
    user = models.CharField(verbose_name='имя')
    email = models.EmailField(verbose_name='почта')

    vacancy = models.ForeignKey('vacancies.vacancy', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True, verbose_name='дата подачи')

    def __str__(self):
        return self.user + ' - ' + self.vacancy.name
