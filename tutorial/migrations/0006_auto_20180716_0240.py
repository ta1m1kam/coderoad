# Generated by Django 2.0.2 on 2018-07-15 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0005_auto_20180710_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='tutorial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tutorial.Tutorial', verbose_name='紐づく記事'),
        ),
    ]