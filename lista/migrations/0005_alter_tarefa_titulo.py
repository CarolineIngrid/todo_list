# Generated by Django 4.0.6 on 2022-07-18 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0004_alter_tarefa_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='titulo',
            field=models.CharField(blank=True, default='', max_length=24, null=True),
        ),
    ]
