# Generated by Django 2.2.5 on 2019-09-10 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_hora_extra', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro_hora_extra',
            name='horas',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
    ]
