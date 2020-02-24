from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    userid = models.CharField(max_length=50, primary_key=True)
    phoneno = models.CharField(max_length=11)

    def __str__(self):
        return self.name
    
class Password(models.Model):
    userid = models.ForeignKey(User, on_delete = models.CASCADE)
    hash = models.CharField(max_length=100)
    
    def __str__(self):
        return self.userid

class Stock(models.Model):
    userid = models.ForeignKey(User, on_delete = models.CASCADE)
    dematAccntNo = models.CharField(max_length=20)
    companyName = models.CharField(max_length=100)
    symbol = models.CharField(max_length=20, primary_key=True)
    value = models.IntegerField
    quantity = models.IntegerField(default=0)
    purchaseCost = models.DecimalField(max_digits=10, decimal_places=2)
    purchaseDate = models.DateTimeField('Date of stock purchase')

    def __str__(self):
        return self.symbol


class Loan(models.Model):
    userid = models.ForeignKey(User, on_delete = models.CASCADE)
    accountNum = models.CharField(max_length=20, primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    rateOfInt = models.IntegerField()
    bankName = models.CharField(max_length=100)
    dueDate = models.DateTimeField('last date for clearence')
    statusofclearence = models.BooleanField(default=True)

    def __str__(self):
        return self.accountNum

class Expenditure(models.Model):
    userid = models.ForeignKey(User, on_delete = models.CASCADE)
    accountNum = models.CharField(max_length=20, primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.CharField(max_length=200)
    transactionDate = models.DateTimeField('date of transaction')

    def __str__(self):
        return self.accountNum

class Savings(models.Model):
    userid = models.ForeignKey(User, on_delete = models.CASCADE)
    accountNum = models.CharField(max_length=20, primary_key=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    rateOfInt = models.IntegerField()
    bankName = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.accountNum