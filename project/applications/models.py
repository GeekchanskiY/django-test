from django.db import models
from django.conf import settings


class Application(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    want_salary = models.IntegerField()

    vacancy = models.ForeignKey('vacancies.vacancy', on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.user:
            return self.user.username + ' - ' + self.vacancy.name
        else:
            return "anonymous" + ' - ' + self.vacancy.name
