# Generated by Django 4.2.20 on 2025-03-19 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0035_add_index_to_agg_alg_tag_proposals'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='difficultytag',
            options={'ordering': ['pk'], 'verbose_name': 'difficulty tag', 'verbose_name_plural': 'difficulty tags'},
        ),
    ]
