from .views import ListDashboard, DetailDashboard
from django.urls import re_path

urlpatterns = [
    re_path(r'^registros/$',ListDashboard.as_view(),name='lista-dash'),
    re_path(r'^registros/(?P<pk>[0-9]+)$',DetailDashboard.as_view(),name='detail-dash'),
]