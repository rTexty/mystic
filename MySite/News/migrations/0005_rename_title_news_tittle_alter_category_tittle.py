# Generated by Django 4.2.5 on 2023-10-09 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_rename_category_news_category_alter_news_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='title',
            new_name='tittle',
        ),
        migrations.AlterField(
            model_name='category',
            name='tittle',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Название категории'),
        ),
    ]
