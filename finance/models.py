from django.db import models
from django.utils import timezone


# Employee related tables
class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile_number = models.BigIntegerField(unique=True)
    create_date = models.DateTimeField().auto_now_add
    last_update = models.DateField().auto_now

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class GivenToEmployee(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    size_a = models.SmallIntegerField()
    size_b = models.SmallIntegerField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.employee_id)


class TakenFromEmployee(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    size_a = models.SmallIntegerField()
    size_b = models.SmallIntegerField()
    paid = models.BooleanField(default=False)
    paid_by_provider = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)


class PendingFromEmployee(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    size_a = models.SmallIntegerField()
    size_b = models.SmallIntegerField()


class EmployeePayment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateTimeField()
    from_period = models.DateTimeField()
    to_period = models.DateTimeField()


class EmployeeAdvance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField()


# Provider related tables
class Provider(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile_number = models.BigIntegerField(unique=True)
    Trading_name = models.CharField(max_length=50)
    create_date = models.DateTimeField().auto_now_add
    last_update = models.DateField().auto_now

    def __str__(self):
        return self.first_name


class GivenToProvider(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    size_a = models.SmallIntegerField()
    size_b = models.SmallIntegerField()
    date = models.DateTimeField(default=timezone.now)


class TakeFromProvider(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    size_a = models.SmallIntegerField()
    size_b = models.SmallIntegerField()
    paid = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)


class PendingToProvider(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    size_a = models.SmallIntegerField()
    size_b = models.SmallIntegerField()


class ProviderPayment(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateTimeField()
    from_period = models.DateTimeField()
    to_period = models.DateTimeField()


class ProviderAdvance(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField()