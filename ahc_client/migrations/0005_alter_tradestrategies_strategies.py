# Generated by Django 4.0.4 on 2022-05-07 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahc_client', '0004_alter_tradestrategies_strategies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradestrategies',
            name='strategies',
            field=models.IntegerField(),
        ),
    ]
