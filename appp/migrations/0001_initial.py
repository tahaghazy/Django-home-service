# Generated by Django 2.2.17 on 2021-02-06 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=40)),
                ('color', models.CharField(choices=[('#f56954', 'Danger'), ('#f39c12', 'Warning'), ('#00a65a', 'Success'), ('#00c0ef', 'Info'), ('#3c8dbc', 'Primary'), ('#d2d6de', 'Gray'), ('#111111', 'Black')], default='#111111', max_length=7)),
                ('content', models.TextField(max_length=200)),
                ('url', models.URLField(blank=True, null=True)),
                ('seen_date', models.DateTimeField(blank=True, editable=False, null=True)),
                ('send_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', related_query_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
