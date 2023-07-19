# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Players(models.Model):
    # Field name made lowercase.
    id = models.TextField(
        db_column='id', blank=True, null=False, primary_key=True)
    years = models.TextField(db_column='Years', blank=True, null=False)
    first = models.TextField(db_column='First', blank=False, null=False)
    last = models.TextField(db_column='Last', blank=False, null=False)
    player = models.TextField(db_column='Player', blank=False, null=False)
    # Field name made lowercase.
    anaheim = models.IntegerField(db_column='Anaheim', blank=True, null=True)
    # Field name made lowercase.
    arizona = models.IntegerField(db_column='Arizona', blank=True, null=True)
    # Field name made lowercase.
    boston = models.IntegerField(db_column='Boston', blank=True, null=True)
    # Field name made lowercase.
    buffalo = models.IntegerField(db_column='Buffalo', blank=True, null=True)
    # Field name made lowercase.
    calgary = models.IntegerField(db_column='Calgary', blank=True, null=True)
    # Field name made lowercase.
    carolina = models.IntegerField(db_column='Carolina', blank=True, null=True)
    # Field name made lowercase.
    chicago = models.IntegerField(db_column='Chicago', blank=True, null=True)
    # Field name made lowercase.
    colorado = models.IntegerField(db_column='Colorado', blank=True, null=True)
    # Field name made lowercase.
    columbus = models.IntegerField(db_column='Columbus', blank=True, null=True)
    # Field name made lowercase.
    dallas = models.IntegerField(db_column='Dallas', blank=True, null=True)
    # Field name made lowercase.
    detroit = models.IntegerField(db_column='Detroit', blank=True, null=True)
    # Field name made lowercase.
    edmonton = models.IntegerField(db_column='Edmonton', blank=True, null=True)
    # Field name made lowercase.
    florida = models.IntegerField(db_column='Florida', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    los_angeles = models.IntegerField(
        db_column='Los Angeles', blank=True, null=True)
    # Field name made lowercase.
    minnesota = models.IntegerField(
        db_column='Minnesota', blank=True, null=True)
    # Field name made lowercase.
    montreal = models.IntegerField(db_column='Montreal', blank=True, null=True)
    # Field name made lowercase.
    nashville = models.IntegerField(
        db_column='Nashville', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    new_jersey = models.IntegerField(
        db_column='New Jersey', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    new_york_islanders = models.IntegerField(
        db_column='New York Islanders', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    new_york_rangers = models.IntegerField(
        db_column='New York Rangers', blank=True, null=True)
    # Field name made lowercase.
    ottawa = models.IntegerField(db_column='Ottawa', blank=True, null=True)
    # Field name made lowercase.
    philadelphia = models.IntegerField(
        db_column='Philadelphia', blank=True, null=True)
    # Field name made lowercase.
    pittsburgh = models.IntegerField(
        db_column='Pittsburgh', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    san_jose = models.IntegerField(db_column='San Jose', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    st_louis = models.IntegerField(
        db_column='St Louis', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    tampa_bay = models.IntegerField(
        db_column='Tampa Bay', blank=True, null=True)
    # Field name made lowercase.
    toronto = models.IntegerField(db_column='Toronto', blank=True, null=True)
    # Field name made lowercase.
    vancouver = models.IntegerField(
        db_column='Vancouver', blank=True, null=True)
    # Field name made lowercase.
    vegas = models.IntegerField(db_column='Vegas', blank=True, null=True)
    # Field name made lowercase.
    washington = models.IntegerField(
        db_column='Washington', blank=True, null=True)
    # Field name made lowercase.
    winnipeg = models.IntegerField(db_column='Winnipeg', blank=True, null=True)
    # Field name made lowercase.
    seattle = models.IntegerField(db_column='Seattle', blank=True, null=True)
    hart = models.IntegerField(blank=True, null=True)
    ladybyng = models.IntegerField(blank=True, null=True)
    vezina = models.IntegerField(blank=True, null=True)
    calder = models.IntegerField(blank=True, null=True)
    artross = models.IntegerField(blank=True, null=True)
    connsmythe = models.IntegerField(blank=True, null=True)
    tedlindsay = models.IntegerField(blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    fiftygoals = models.IntegerField(
        db_column='fiftygoals', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    hundredpoints = models.IntegerField(
        db_column='hundredpoints', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    seventyassists = models.IntegerField(
        db_column='seventyassists', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    fiveshutouts = models.IntegerField(
        db_column='fiveshutouts', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    firstoverall = models.IntegerField(
        db_column='firstoverall', blank=True, null=True)
    topten = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Players'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
