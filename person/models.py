from django.db import models


MAX_LENGTH = 50
NAME_LENGTH = 100
POSITION_LENGTH = 50
SALARY_DIGITS = 10
SALARY_DIGITS_DECIMAL = 2


class Department(models.Model):
    name = models.CharField('Наименование', max_length=NAME_LENGTH)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Вышестоящее подразделение'
    )

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    def __str__(self):
        return (
            f'{self.name} / {self.parent}' if self.parent else f'{self.name}'
        )[:MAX_LENGTH]


class Employee(models.Model):
    full_name = models.CharField('ФИО', max_length=NAME_LENGTH)
    position = models.CharField('Должность', max_length=POSITION_LENGTH)
    hire_date = models.DateField('Дата')
    salary = models.DecimalField('Оклад',
                                 max_digits=SALARY_DIGITS,
                                 decimal_places=SALARY_DIGITS_DECIMAL)
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
