# Generated by Django 4.2.4 on 2023-08-28 11:46

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('text', models.TextField(max_length=2000)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bookstore.book')),
            ],
        ),
    ]
