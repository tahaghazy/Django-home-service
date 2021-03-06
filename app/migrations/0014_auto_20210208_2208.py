# Generated by Django 2.2.17 on 2021-02-08 20:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20210208_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='siteedit',
            old_name='adrress',
            new_name='address',
        ),
        migrations.AddField(
            model_name='siteedit',
            name='img',
            field=models.ImageField(default='image.png', upload_to='', verbose_name='صورة من نحن'),
        ),
        migrations.AlterField(
            model_name='help',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='تاريخ الارسال'),
        ),
    ]
