# Generated by Django 2.2.17 on 2021-02-07 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-id'], 'verbose_name': 'اشعار', 'verbose_name_plural': 'الاشعارات'},
        ),
        migrations.AlterField(
            model_name='notification',
            name='color',
            field=models.CharField(choices=[('#f56954', 'Danger'), ('#f39c12', 'Warning'), ('#00a65a', 'Success'), ('#00c0ef', 'Info'), ('#3c8dbc', 'Primary'), ('#d2d6de', 'Gray'), ('#111111', 'Black')], default='#111111', editable=False, max_length=7),
        ),
        migrations.AlterField(
            model_name='notification',
            name='icon',
            field=models.CharField(editable=False, max_length=40),
        ),
        migrations.AlterField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='notifications', related_query_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
