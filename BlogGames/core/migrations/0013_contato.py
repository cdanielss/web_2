# Generated by Django 3.1.4 on 2021-11-20 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20211119_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(default='c@c.com', max_length=50)),
                ('tipo', models.CharField(default='', max_length=50)),
                ('mensagem', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
