# Generated by Django 4.2.3 on 2023-07-10 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codename', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('first_name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
                ('action_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.TextField(blank=True, db_column='Player', null=True)),
                ('anaheim', models.IntegerField(blank=True, db_column='Anaheim', null=True)),
                ('arizona', models.IntegerField(blank=True, db_column='Arizona', null=True)),
                ('boston', models.IntegerField(blank=True, db_column='Boston', null=True)),
                ('buffalo', models.IntegerField(blank=True, db_column='Buffalo', null=True)),
                ('calgary', models.IntegerField(blank=True, db_column='Calgary', null=True)),
                ('carolina', models.IntegerField(blank=True, db_column='Carolina', null=True)),
                ('chicago', models.IntegerField(blank=True, db_column='Chicago', null=True)),
                ('colorado', models.IntegerField(blank=True, db_column='Colorado', null=True)),
                ('columbus', models.IntegerField(blank=True, db_column='Columbus', null=True)),
                ('dallas', models.IntegerField(blank=True, db_column='Dallas', null=True)),
                ('detroit', models.IntegerField(blank=True, db_column='Detroit', null=True)),
                ('edmonton', models.IntegerField(blank=True, db_column='Edmonton', null=True)),
                ('florida', models.IntegerField(blank=True, db_column='Florida', null=True)),
                ('los_angeles', models.IntegerField(blank=True, db_column='Los Angeles', null=True)),
                ('minnesota', models.IntegerField(blank=True, db_column='Minnesota', null=True)),
                ('montreal', models.IntegerField(blank=True, db_column='Montreal', null=True)),
                ('nashville', models.IntegerField(blank=True, db_column='Nashville', null=True)),
                ('new_jersey', models.IntegerField(blank=True, db_column='New Jersey', null=True)),
                ('new_york_islanders', models.IntegerField(blank=True, db_column='New York Islanders', null=True)),
                ('new_york_rangers', models.IntegerField(blank=True, db_column='New York Rangers', null=True)),
                ('ottawa', models.IntegerField(blank=True, db_column='Ottawa', null=True)),
                ('philadelphia', models.IntegerField(blank=True, db_column='Philadelphia', null=True)),
                ('pittsburgh', models.IntegerField(blank=True, db_column='Pittsburgh', null=True)),
                ('san_jose', models.IntegerField(blank=True, db_column='San Jose', null=True)),
                ('st_louis', models.IntegerField(blank=True, db_column='St. Louis', null=True)),
                ('tampa_bay', models.IntegerField(blank=True, db_column='Tampa Bay', null=True)),
                ('toronto', models.IntegerField(blank=True, db_column='Toronto', null=True)),
                ('vancouver', models.IntegerField(blank=True, db_column='Vancouver', null=True)),
                ('vegas', models.IntegerField(blank=True, db_column='Vegas', null=True)),
                ('washington', models.IntegerField(blank=True, db_column='Washington', null=True)),
                ('winnipeg', models.IntegerField(blank=True, db_column='Winnipeg', null=True)),
                ('seattle', models.IntegerField(blank=True, db_column='Seattle', null=True)),
                ('hart', models.IntegerField(blank=True, null=True)),
                ('ladybyng', models.IntegerField(blank=True, null=True)),
                ('vezina', models.IntegerField(blank=True, null=True)),
                ('calder', models.IntegerField(blank=True, null=True)),
                ('artross', models.IntegerField(blank=True, null=True)),
                ('connsmythe', models.IntegerField(blank=True, null=True)),
                ('tedlindsay', models.IntegerField(blank=True, null=True)),
                ('number_50goals', models.IntegerField(blank=True, db_column='50goals', null=True)),
                ('number_100points', models.IntegerField(blank=True, db_column='100points', null=True)),
                ('number_70assists', models.IntegerField(blank=True, db_column='70assists', null=True)),
                ('number_5shutouts', models.IntegerField(blank=True, db_column='5shutouts', null=True)),
                ('number_1st', models.IntegerField(blank=True, db_column='1st', null=True)),
                ('top10', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Players',
                'managed': False,
            },
        ),
    ]
