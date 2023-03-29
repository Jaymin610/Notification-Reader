# Generated by Django 4.0.4 on 2023-03-24 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(blank=True, max_length=30, null=True)),
                ('androidid', models.CharField(blank=True, max_length=40, null=True, unique=True)),
                ('androidid1', models.CharField(blank=True, max_length=40, null=True, unique=True)),
                ('androidid2', models.CharField(blank=True, max_length=40, null=True, unique=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=20, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('androidid', models.CharField(blank=True, max_length=40, null=True)),
                ('title', models.CharField(blank=True, max_length=64, null=True)),
                ('msg', models.CharField(blank=True, max_length=512, null=True)),
                ('package', models.CharField(blank=True, max_length=10, null=True)),
                ('RegDate', models.DateField(blank=True, null=True)),
                ('ntime', models.TimeField(blank=True, null=True)),
                ('reciveDate', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationDetais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('androidid', models.CharField(blank=True, max_length=40, null=True)),
                ('androidid1', models.CharField(blank=True, max_length=40, null=True)),
                ('androidid2', models.CharField(blank=True, max_length=40, null=True)),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(blank=True, max_length=30, null=True)),
                ('date', models.DateField()),
                ('ntime', models.TimeField(blank=True, null=True)),
                ('ncount', models.IntegerField(default=0)),
            ],
        ),
    ]