# Generated by Django 2.2 on 2020-05-31 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200531_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friends',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.UserProfile', unique=True),
        ),
    ]
