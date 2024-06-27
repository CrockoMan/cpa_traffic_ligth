from django.db import models

MAX_LENGTH = 30

class Department(models.Model):
    name = models.CharField('Наименование', max_length=100)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Иерархия'
    )

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    def __str__(self):
        return (
            f'{self.parent} / {self.name}' if self.parent else f'{self.name}'
        )[:MAX_LENGTH]



class Employee(models.Model):
    full_name = models.CharField('ФИО', max_length=100)
    position = models.CharField('Должность', max_length=50)
    hire_date = models.DateField('Дата')
    salary = models.DecimalField('Оклад', max_digits=10, decimal_places=2)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        verbose_name='Подразделение'
    )

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.full_name} {self.position}'[:MAX_LENGTH]
