# Generated by Django 2.2.1 on 2019-09-12 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20190912_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('gender', models.SmallIntegerField()),
                ('person', models.ManyToManyField(to='app01.Person')),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
    ]
