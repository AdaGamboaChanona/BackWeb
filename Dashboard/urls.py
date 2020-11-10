from .views import generalDashboard, EspecificoDashboard
from django.urls import re_path

urlpatterns = [
    re_path(r'^registrosGeneralDash/$',generalDashboard.as_view(),name='lista-dash'),
    re_path(r'^registrosEspecificosDash/(?P<pk>[0-9]+)$',EspecificoDashboard.as_view(),name='detail-dash'),
]