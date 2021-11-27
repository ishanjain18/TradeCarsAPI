# Generated by Django 3.2.9 on 2021-11-26 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Sellers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_year', models.PositiveSmallIntegerField()),
                ('min_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('max_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_site.companies')),
                ('model_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_site.cars')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_site.sellers')),
            ],
        ),
        migrations.AddField(
            model_name='cars',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_site.companies'),
        ),
    ]
