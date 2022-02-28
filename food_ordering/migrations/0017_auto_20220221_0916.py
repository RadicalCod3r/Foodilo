# Generated by Django 2.2.12 on 2022-02-21 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_ordering', '0016_auto_20220219_1513'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Addresses'},
        ),
        migrations.AlterField(
            model_name='account',
            name='bank_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='food_ordering.Bank'),
        ),
        migrations.AlterField(
            model_name='account',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='food_ordering.User'),
        ),
        migrations.AlterField(
            model_name='address',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='food_ordering.User'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='food_ordering.Customer'),
        ),
        migrations.AlterField(
            model_name='courier',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='food_ordering.User'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='food_ordering.User'),
        ),
        migrations.AlterField(
            model_name='food',
            name='resturant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='food_ordering.Resturant'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='food_ordering.User'),
        ),
        migrations.AlterField(
            model_name='resturant',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='food_ordering.User'),
        ),
    ]
