# Generated by Django 4.0.2 on 2022-02-06 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0002_pizza_cena_pizza_skladniki_alter_pizza_nazwa'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='zdjecie',
            field=models.ImageField(blank=True, null=True, upload_to='foty'),
        ),
    ]
