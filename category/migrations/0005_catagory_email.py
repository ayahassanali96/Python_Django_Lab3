# Generated by Django 4.1.6 on 2023-02-07 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_alter_catagory_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='email',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]