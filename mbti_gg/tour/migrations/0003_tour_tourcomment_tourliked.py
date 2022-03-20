# Generated by Django 3.1.3 on 2022-03-20 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mbti', '0001_initial'),
        ('user', '0005_auto_20220309_1836'),
        ('tour', '0002_auto_20220320_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('tour_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('info', models.TextField(blank=True, null=True)),
                ('photo', models.TextField(blank=True, null=True)),
                ('user_id', models.ForeignKey(db_column='user_id', default='admin', on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='TourLiked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_user', models.ManyToManyField(blank=True, related_name='like_user_tour', to='user.User')),
                ('tour_id', models.ForeignKey(db_column='tour_id', on_delete=django.db.models.deletion.CASCADE, to='tour.tour')),
            ],
        ),
        migrations.CreateModel(
            name='TourComment',
            fields=[
                ('h_cno', models.BigAutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('mbti_id', models.ForeignKey(db_column='mbti_id', on_delete=django.db.models.deletion.CASCADE, to='mbti.mbti')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]