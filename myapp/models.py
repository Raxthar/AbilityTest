from django.db import models

# Create your models here.


class ATest(models.Model):
    tID = models.IntegerField(primary_key=True, db_column='FId')
    tName = models.CharField(max_length=30)
    tDescribe = models.CharField(max_length=80)


class Question(models.Model):
    qID = models.IntegerField(primary_key=True, db_column='FId')
    qName = models.CharField(max_length=30)
    tID = models.ForeignKey(ATest, on_delete=models.CASCADE)


class Dimension(models.Model):
    dID = models.IntegerField(primary_key=True, db_column='FId')
    dName = models.CharField(max_length=30)
    tID = models.ForeignKey(ATest, on_delete=models.CASCADE)


class Option(models.Model):
    oID = models.IntegerField(primary_key=True, db_column='FId')
    oName = models.CharField(max_length=30)
    qID = models.ForeignKey(Question, on_delete=models.CASCADE)
    score = models.IntegerField()
    dID = models.ForeignKey(Dimension, on_delete=models.CASCADE)