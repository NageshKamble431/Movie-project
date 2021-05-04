# Generated by Django 3.1.3 on 2021-05-03 18:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('title', models.CharField(max_length=300)),
                ('discription', models.CharField(max_length=300)),
                ('genres', models.CharField(max_length=300)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]