# Generated by Django 3.2.5 on 2022-03-08 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20220308_1417'),
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', default='admin', on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]
