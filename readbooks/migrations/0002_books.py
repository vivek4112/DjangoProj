# Generated by Django 2.1 on 2018-08-06 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readbooks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=64)),
                ('author', models.CharField(max_length=64)),
                ('year', models.IntegerField()),
            ],
        ),
    ]