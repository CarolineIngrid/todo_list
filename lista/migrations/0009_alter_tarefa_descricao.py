# Generated by Django 4.0.6 on 2022-07-21 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0008_alter_tarefa_categoria_alter_tarefa_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='descricao',
            field=models.TextField(blank=True),
        ),
    ]