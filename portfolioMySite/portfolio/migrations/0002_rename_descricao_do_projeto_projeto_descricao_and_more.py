# Generated by Django 4.0.4 on 2022-04-24 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projeto',
            old_name='descricao_do_projeto',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='projeto',
            old_name='linguagem_utilizada',
            new_name='linguagem',
        ),
        migrations.RenameField(
            model_name='projeto',
            old_name='repositorio_do_projeto',
            new_name='repositorio',
        ),
    ]
