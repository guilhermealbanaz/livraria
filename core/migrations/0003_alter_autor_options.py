# Generated by Django 4.0.5 on 2022-07-08 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_autor_editora_livro'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name_plural': 'Autores'},
        ),
    ]
