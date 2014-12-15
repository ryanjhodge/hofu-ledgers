# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from __future__ import unicode_literals

from django.db import models

class Labordyn(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')
    lastname = models.CharField(max_length=60, db_column='LASTNAME', blank=True)
    firstname = models.CharField(max_length=50, db_column='FIRSTNAME', blank=True)
    gender = models.CharField(max_length=1, db_column='GENDER', blank=True)
    race = models.CharField(max_length=1, db_column='RACE', blank=True)
    occup1 = models.CharField(max_length=60, db_column='OCCUP1', blank=True)
    occup2 = models.CharField(max_length=60, db_column='OCCUP2', blank=True)
    occup3 = models.CharField(max_length=60, db_column='OCCUP3', blank=True)
    occup4 = models.CharField(max_length=60, db_column='OCCUP4', blank=True)
    occup5 = models.CharField(max_length=30, db_column='OCCUP5', blank=True)
    tenurefrom = models.DateField(null=True, db_column='TENUREFROM', blank=True)
    tenureto = models.DateField(null=True, db_column='TENURETO', blank=True)
    tenurefr2 = models.DateField(null=True, db_column='TENUREFR2', blank=True)
    tenureto2 = models.DateField(null=True, db_column='TENURETO2', blank=True)
    tenurefr3 = models.DateField(null=True, db_column='TENUREFR3', blank=True)
    tenureto3 = models.DateField(null=True, db_column='TENURETO3', blank=True)
    tenureto3a = models.DateField(null=True, db_column='TENURETO3a', blank=True)
    #sources = models.CharField(max_length=255, db_column='SOURCES', blank=True)
    notes = models.TextField(db_column='NOTES', blank=True)
    #begin = models.CharField(max_length=50, db_column='BEGIN', blank=True)
    #end = models.CharField(max_length=50, db_column='END', blank=True)
    
    def __unicode__(self):
        return unicode(self.lastname)
    
    class Meta:
        db_table = 'LABORDYN'

