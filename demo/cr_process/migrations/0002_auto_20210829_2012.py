# Generated by Django 3.2.6 on 2021-08-29 19:12

import demo.cr_process.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cr_process', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crprocess',
            name='l1_approve_comment',
            field=models.CharField(max_length=1024, null=True, verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='crprocess',
            name='l2_approve_comment',
            field=models.CharField(max_length=1024, null=True, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='crprocess',
            name='affected_device',
            field=models.CharField(max_length=128, verbose_name='Affected Device'),
        ),
        migrations.AlterField(
            model_name='crprocess',
            name='cr_type',
            field=models.CharField(choices=[('FM', 'Fault Mgt'), ('PR', 'Preventive'), ('AD', 'Adaptive'), ('PF', 'Perfective')], max_length=128, verbose_name='CR Type'),
        ),
        migrations.AlterField(
            model_name='crprocess',
            name='l1_approve',
            field=models.CharField(choices=[('AP', 'Approve'), ('DN', 'Deny')], max_length=128, verbose_name='L1 Approval'),
        ),
        migrations.AlterField(
            model_name='crprocess',
            name='l2_approve',
            field=models.CharField(choices=[('AP', 'Approve'), ('DN', 'Deny')], max_length=128, verbose_name='L2 Approval'),
        ),
        migrations.AlterField(
            model_name='crprocess',
            name='orderid',
            field=models.CharField(default=demo.cr_process.models.get_crid, max_length=32, unique=True, verbose_name='Order ID'),
        ),
        migrations.AlterField(
            model_name='crprocess',
            name='product_name',
            field=models.CharField(choices=[('CC', 'Cisco'), ('JP', 'Juniper'), ('AWS', 'AWS'), ('AZ', 'Azure')], max_length=128, verbose_name='Product Name'),
        ),
        migrations.AlterField(
            model_name='crprocess',
            name='severity',
            field=models.CharField(choices=[('SD', 'Standard'), ('NM', 'Normal'), ('MJ', 'Major'), ('EM', 'Emergency')], max_length=128),
        ),
        migrations.AlterField(
            model_name='crprocess',
            name='vendor',
            field=models.CharField(choices=[('OS', 'On-Site'), ('CL', 'Cloud')], max_length=128),
        ),
    ]
