from django.db import models


class DashboardModel(models.Model):
    nombreCompleto = models.CharField(max_length=50)
    edad = models.IntegerField()
    correo = models.CharField(max_length=50)

    def _str_(self):
        return self.nombreCompleto
