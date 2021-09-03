from django.urls import path
from django.urls.conf import re_path

from . import views

app_name = "employees"
urlpatterns = [
    re_path(r"^employee$", views.employee_list),
    re_path(r"^employee/(?P<pk>[0-9]+)$", views.employee_detail),
    re_path(r"^employee/departments$", views.employee_departments),
]
