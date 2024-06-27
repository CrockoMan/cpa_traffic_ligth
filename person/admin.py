from django.contrib import admin

from person.models import Department, Employee

admin.site.register(Department)
admin.site.register(Employee)
