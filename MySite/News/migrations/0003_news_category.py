# Generated by Django 4.2.5 on 2023-10-09 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='Category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='news.category'),
        ),
    ]
