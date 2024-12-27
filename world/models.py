from django.db import models
class Currency(models.Model):
    Code=models.CharField( max_length=3, primary_key=True)
    Currency=models.CharField(max_length=25)
    IsActive=models.BooleanField(max_length=1, default=True)

    def _str_(self):
        return self.Currency
    
class Country(models.Model):
    Code=models.CharField(max_length=3, primary_key=True)
    Country=models.CharField(max_length=25)
    Currency=models.ForeignKey(Currency, on_delete=models.CASCADE)
    IsActive=models.BooleanField(max_length=1, default=True)


    def _str_(self):
            return self.Country
