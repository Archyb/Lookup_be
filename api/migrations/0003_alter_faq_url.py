# Generated by Django 4.1.4 on 2022-12-15 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_faq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='url',
            field=models.CharField(max_length=250),
        ),
    ]
