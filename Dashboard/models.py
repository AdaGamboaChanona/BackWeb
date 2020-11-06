from django.db import models


class DashboardModel(models.Model):
    nombreCompleto = models.CharField(max_length=50)
    edad = models.CharField(max_length=10)
    correo = models.CharField(max_length=50)

    def _str_(self):
        return self.nombreCompleto
