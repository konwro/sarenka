# Generated by Django 3.0.6 on 2020-09-26 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_base', '0013_auto_20200926_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cwemodel',
            name='rank',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (None, '-1')], default=None, max_length=2, null=True),
        ),
    ]
