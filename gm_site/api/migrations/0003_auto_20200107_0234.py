# Generated by Django 3.0.2 on 2020-01-07 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200105_0421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='streamfield',
            name='article_id',
        ),
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='ContentStreamField',
        ),
        migrations.DeleteModel(
            name='StreamField',
        ),
    ]