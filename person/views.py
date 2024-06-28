from collections import namedtuple
from django.shortcuts import render

from person.models import Department, Employee


DepartmentNode = namedtuple(
    'namedtuple',
    ('department', 'children', 'employees')
)


def employee_department_view(request):
    departments = Department.objects.all()
    employees = Employee.objects.all()

    department_hierarchy = {}
    for department in departments:
        department_hierarchy[department.pk] = []
    tops = []
    for department in departments:
        if department.parent is not None:
            sibglings = department_hierarchy[department.parent.pk]
            sibglings.append(department)
        else:
            tops.append(department)

    def fill_tree(dep_node):
        child_deps = department_hierarchy.get(dep_node.department.pk)
        if not child_deps:
            child_deps = []
        for child_dep in child_deps:
            child_node = DepartmentNode(child_dep, [], [])
            fill_tree(child_node)
            dep_node.children.append(child_node)
        dep_employees = (
            emp for emp in employees
            if emp.department.pk == dep_node.department.pk
        )
        dep_node.employees.extend(dep_employees)

    departments_tree = []
    for top in tops:
        top_node = DepartmentNode(top, [], [])
        fill_tree(top_node)
        departments_tree.append(top_node)

    context = {
        'departments': tops,
        'departments_tree': departments_tree,
        'employees': employees,
    }

    return render(request, 'person/employee_department.html', context)
