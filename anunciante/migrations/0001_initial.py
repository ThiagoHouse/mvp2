# Generated by Django 2.2.2 on 2019-06-17 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anunciante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('senha', models.TextField()),
                ('email', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
