from django.db import models

class StockData(models.Model):
    date = models.AutoField(primary_key=True)
    top30 = models.CharField(max_length=45)
    title = models.CharField(max_length=45)
    rate = models.CharField(max_length=45)
    content = models.CharField(max_length=45)
    tags = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'stockdata'
