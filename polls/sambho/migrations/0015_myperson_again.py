# Generated by Django 4.0.4 on 2022-05-03 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sambho', '0014_person_oncemore_myperson_orderedperson'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyPerson_again',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('sambho.person_oncemore',),
        ),
    ]
