# Generated by Django 2.2.2 on 2019-07-17 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0014_auto_20190717_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='hash_code',
            field=models.CharField(default='mEQvLPYIjC2xM35SHX46qZCNnyUslDOaCoK4ZXgesrqQ9L6IElR2oGv4F6F7r8mN', max_length=64, unique=True),
        ),
    ]