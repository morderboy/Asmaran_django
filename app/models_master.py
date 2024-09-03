CSRF_COOKIE_SECURE: False
SESSION_COOKIE_SECURE: False
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    username = models.CharField(unique=True, max_length=228, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    activated = models.IntegerField(blank=True, null=True)
    suspended = models.IntegerField(blank=True, null=True)
    activation_key = models.CharField(max_length=32, blank=True, null=True)
    current_world_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    last_modified_at = models.DateTimeField(blank=True, null=True)
    coin_current = models.IntegerField()
    coin_total = models.IntegerField()
    external_id = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account'


class Vip(models.Model):
    account_id = models.IntegerField(primary_key=True)
    character_oid = models.IntegerField()
    world = models.CharField(max_length=20)
    vip_level = models.IntegerField()
    vip_expire = models.BigIntegerField()
    vip_points = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vip'

