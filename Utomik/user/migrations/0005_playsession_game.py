# Generated by Django 3.1.4 on 2020-12-28 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20201227_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='playsession',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.game'),
        ),
    ]
