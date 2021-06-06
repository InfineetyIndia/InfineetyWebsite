# Generated by Django 3.2 on 2021-06-06 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_plantype_display_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='active_status',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='transaction',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plan', to='payments.plan'),
        ),
    ]
