# Generated by Django 3.2.7 on 2022-08-27 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20220828_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='auther',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app1.customer_class'),
        ),
    ]
