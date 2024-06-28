from django.db import models


MAX_LEN = 50
NAME_LEN = 100
POSITION_LEN = 50
SALARY_DIGITS = 10
SALARY_DIGITS_DECIMAL = 2


class Department(models.Model):
    name = models.CharField('Наименование', max_length=NAME_LEN)
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
        )[:MAX_LEN]


class Position(models.Model):
    position = models.CharField('Должность', max_length=POSITION_LEN)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return f'{self.position}'[:MAX_LEN]


class Employee(models.Model):
    full_name = models.CharField('ФИО', max_length=NAME_LEN)
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        verbose_name='Должность'
    )
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
        return f'{self.full_name} {self.position}'[:MAX_LEN]
