# Generated by Django 2.2.4 on 2019-08-31 21:31

from django.db import migrations, models
import vouchers.models


class Migration(migrations.Migration):

    dependencies = [
        ('vouchers', '0004_auto_20190831_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher',
            name='code',
            field=models.CharField(default=vouchers.models.generate_code, editable=False, max_length=12),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='remaining_uses',
            field=models.IntegerField(default=3, editable=False),
        ),
    ]
