from django.db import models

# Create your models here.


class User(models.Model):
    u_id = models.AutoField(primary_key=True, db_column='u_id')
    u_name = models.CharField(max_length=30)


class ATest(models.Model):
    t_id = models.AutoField(primary_key=True, db_column='t_id')
    t_name = models.CharField(max_length=30)
    t_describe = models.CharField(max_length=80)
    u_id = models.IntegerField()
    t_status = models.IntegerField()
    t_due = models.CharField(max_length=80)


class Question(models.Model):
    q_id = models.AutoField(primary_key=True, db_column='q_id')
    q_name = models.CharField(max_length=30)
    t_id = models.IntegerField()


class Dimension(models.Model):
    d_id = models.AutoField(primary_key=True, db_column='d_id')
    d_name = models.CharField(max_length=30)
    t_id = models.IntegerField()


class Option(models.Model):
    o_id = models.AutoField(primary_key=True, db_column='o_id')
    o_name = models.CharField(max_length=30)
    q_id = models.IntegerField()
    score = models.IntegerField()
    d_id = models.IntegerField()


class Judge(models.Model):
    j_id = models.AutoField(primary_key=True, db_column='j_id')
    j_content = models.CharField(max_length=200)
    t_id = models.IntegerField()
    d_id = models.IntegerField()


class Record(models.Model):
    record_id = models.AutoField(primary_key=True, db_column='record_id')
    t_id = models.IntegerField()
    q_id = models.IntegerField()
    o_id = models.IntegerField()


class Result(models.Model):
    result_id = models.AutoField(primary_key=True, db_column='result_id')
    t_id = models.IntegerField()
    d_id = models.IntegerField()