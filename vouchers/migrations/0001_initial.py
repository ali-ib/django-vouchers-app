# Generated by Django 2.2.4 on 2019-08-29 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200)),
                ('remaining_uses', models.IntegerField(default=1)),
                ('discount', models.IntegerField(choices=[(1, 'RM 10'), (2, '10% off')], default=1)),
            ],
        ),
    ]
