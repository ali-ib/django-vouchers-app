# Generated by Django 2.2.4 on 2019-08-30 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vouchers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher',
            name='code',
            field=models.CharField(editable=False, max_length=12),
        ),
    ]