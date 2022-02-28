# Generated by Django 2.2.12 on 2022-02-19 13:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_ordering', '0008_auto_20220219_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='bank_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_ordering.Bank'),
        ),
        migrations.AlterField(
            model_name='account',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_ordering.User'),
        ),
        migrations.AlterField(
            model_name='address',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='food_ordering.User'),
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
            model_name='phone',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='food_ordering.User'),
        ),
        migrations.AlterField(
            model_name='resturant',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='food_ordering.User'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_ordering.User')),
                ('resturant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_ordering.Resturant')),
            ],
        ),
    ]