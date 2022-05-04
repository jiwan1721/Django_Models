# Generated by Django 4.0.4 on 2022-05-02 04:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sambho', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='baseModel',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sambho.basemodel')),
                ('color_code', models.CharField(max_length=100)),
            ],
            bases=('sambho.basemodel',),
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sambho.basemodel')),
                ('name', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('colors', models.ManyToManyField(to='sambho.color')),
            ],
            bases=('sambho.basemodel',),
        ),
        migrations.CreateModel(
            name='PeopleAddress',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sambho.basemodel')),
                ('address', models.TextField()),
                ('peoples', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='sambho.people')),
            ],
            bases=('sambho.basemodel',),
        ),
    ]
