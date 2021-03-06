# Generated by Django 2.2.12 on 2022-02-19 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_ordering', '0011_auto_20220219_1420'),
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
            model_name='comment',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_ordering.User'),
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
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('courier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_ordering.Courier')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_ordering.Customer')),
                ('food_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_ordering.Food')),
            ],
        ),
    ]
