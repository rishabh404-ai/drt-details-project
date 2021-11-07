# Generated by Django 3.2.9 on 2021-11-07 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_property_details_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Petitioner_Detail_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=200, null=True)),
                ('petitioner_details', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Respondents_Details_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=200, null=True)),
                ('respondents_details', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
