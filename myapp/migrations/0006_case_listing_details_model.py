# Generated by Django 3.2.9 on 2021-11-07 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_petitioner_detail_model_petitioner_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case_Listing_Details_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=200, null=True)),
                ('case_listing_details', models.TextField(blank=True, null=True)),
            ],
        ),
    ]