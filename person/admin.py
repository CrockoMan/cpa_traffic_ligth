from django.contrib import admin

from person.models import Department, Employee, Position

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Position)
