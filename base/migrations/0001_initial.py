# Generated by Django 4.0.5 on 2022-06-17 20:20

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=100, validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(100)])),
                ('registry_number', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1000000), django.core.validators.MaxValueValidator(9999999)])),
                ('establishment_date', models.DateField(validators=[django.core.validators.MaxValueValidator(datetime.date(2022, 6, 17))])),
                ('total_capital', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2500)])),
            ],
        ),
        migrations.CreateModel(
            name='BusinessUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_user_name', models.CharField(max_length=100)),
                ('registry_number', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1000000), django.core.validators.MaxValueValidator(9999999)])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('identification_code', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2500)])),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_founder', models.BooleanField()),
                ('is_business_user', models.BooleanField()),
                ('business_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business_user', to='base.user')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.user')),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capital_size', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.business')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.owner')),
            ],
            options={
                'unique_together': {('business', 'owner')},
            },
        ),
    ]