# Generated by Django 2.1.7 on 2019-03-19 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lovelace', '0012_perfilusuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='estabelecimento',
            name='imagem',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='estabelecimento',
            name='telefone_estabelecimento',
            field=models.CharField(max_length=20),
        ),
    ]