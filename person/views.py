from django.shortcuts import render

from person.models import Department, Employee


def employee_department_view(request):
    departments = Department.objects.all()
    employees = Employee.objects.all()

    context = {
        'departments': departments,
        'employees': employees,
    }

    return render(request, 'person/employee_department.html', context)
