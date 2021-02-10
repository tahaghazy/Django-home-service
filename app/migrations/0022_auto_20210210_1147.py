# Generated by Django 2.2.17 on 2021-02-10 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20210210_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteedit',
            name='script',
            field=models.TextField(blank=True, help_text='هذا حقل اكواد اضافيه لموقعك كحقل تحقق احصائيات جوجل مثلا', null=True, verbose_name='اكواد اضافيه'),
        ),
        migrations.AlterField(
            model_name='siteedit',
            name='img3',
            field=models.ImageField(default='image.png', help_text='يفضل ان يكون 543 * 555', upload_to='', verbose_name='صورة وصف الموقع'),
        ),
        migrations.AlterField(
            model_name='siteedit',
            name='img4',
            field=models.ImageField(default='image.png', help_text='يفضل ان يكون 630 * 1920', upload_to='', verbose_name='صورة السلايدر1'),
        ),
        migrations.AlterField(
            model_name='siteedit',
            name='img5',
            field=models.ImageField(default='image.png', help_text='يفضل ان يكون 451 * 1920', upload_to='', verbose_name='صورة السلايدر2'),
        ),
        migrations.AlterField(
            model_name='siteedit',
            name='img6',
            field=models.ImageField(default='image.png', help_text='يفضل ان يكون 630 * 1920', upload_to='', verbose_name='صورة السلايدر3'),
        ),
    ]
