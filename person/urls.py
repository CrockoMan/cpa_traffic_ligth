from django.urls import path
from person import views


app_name = 'person'

urlpatterns = [
    path('', views.employee_department_view, name='persons'),
]
