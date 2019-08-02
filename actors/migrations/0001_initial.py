# Generated by Django 2.2.3 on 2019-07-27 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('dp', models.CharField(blank=True, max_length=512, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
