# Generated by Django 4.2.5 on 2023-11-02 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0005_alter_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]