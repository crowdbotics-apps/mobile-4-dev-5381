# Generated by Django 2.2.13 on 2020-06-04 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_fnhgjhjgjh'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtext',
            name='dfsasa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customtext_dfsasa', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customtext',
            name='fdgg',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customtext',
            name='sadfasf',
            field=models.ManyToManyField(blank=True, related_name='customtext_sadfasf', to='home.Fnhgjhjgjh'),
        ),
        migrations.AddField(
            model_name='customtext',
            name='sasfsdf',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customtext_sasfsdf', to='home.Test'),
        ),
        migrations.AddField(
            model_name='customtext',
            name='sdfdsf',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customtext_sdfdsf', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customtext',
            name='sdfsdf',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
