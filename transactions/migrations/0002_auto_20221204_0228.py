# Generated by Django 3.1.8 on 2022-12-03 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Deposit'), (2, 'Withdrawal'), (3, 'Interest'), (0, 'Home'), (0, 'contact'), (0, 'about'), (0, 'feedback')]),
        ),
    ]
