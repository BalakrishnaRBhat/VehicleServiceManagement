# Generated by Django 2.2.4 on 2019-11-08 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('cust_phone', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=100)),
                ('cust_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_reg_no', models.CharField(max_length=10)),
                ('vehicle_name', models.CharField(max_length=50)),
                ('vehicle_type', models.CharField(max_length=20)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vehdoc.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('ss_phone', models.CharField(max_length=12)),
                ('stat_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_service', models.CharField(max_length=50, null=True)),
                ('service_desc', models.CharField(max_length=100, null=True)),
                ('ser_status', models.CharField(choices=[('Waiting', 'Waiting'), ('In progress', 'In progress'), ('Completed', 'Completed')], max_length=100, null=True)),
                ('start_date', models.DateTimeField(null=True)),
                ('finish_date', models.DateTimeField(null=True)),
                ('ser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Vehdoc.ServiceStation')),
                ('ss', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vehdoc.Customer')),
                ('veh', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Vehdoc.Vehicle')),
            ],
        ),
    ]
