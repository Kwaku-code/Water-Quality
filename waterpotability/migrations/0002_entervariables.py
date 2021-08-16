# Generated by Django 3.2.6 on 2021-08-11 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waterpotability', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnterVariables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ph', models.FloatField(default=0.0)),
                ('Hardness', models.FloatField(default=0.0)),
                ('Solids', models.FloatField(default=0.0)),
                ('Chloramines', models.FloatField(default=0.0)),
                ('Sulfate', models.FloatField(default=0.0)),
                ('Conductivity', models.FloatField(default=0.0)),
                ('Organic_carbon', models.FloatField(default=0.0)),
                ('Trihalomethanes', models.FloatField(default=0.0)),
                ('Turbidity', models.FloatField(default=0.0)),
            ],
        ),
    ]
