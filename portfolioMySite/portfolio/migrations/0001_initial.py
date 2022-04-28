# Generated by Django 4.0.4 on 2022-04-24 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Linguagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linguagem_nome', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['linguagem_nome'],
            },
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_projeto', models.CharField(max_length=40)),
                ('descricao_do_projeto', models.TextField(blank=True, null=True)),
                ('repositorio_do_projeto', models.CharField(default='Sem repositório.', max_length=60)),
                ('imagem_ilustrativa', models.ImageField(blank=True, upload_to='static/portfolio/img')),
                ('linguagem_utilizada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.linguagem')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]