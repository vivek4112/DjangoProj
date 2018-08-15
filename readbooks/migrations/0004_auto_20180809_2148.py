# Generated by Django 2.1 on 2018-08-10 01:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('readbooks', '0003_auto_20180809_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]