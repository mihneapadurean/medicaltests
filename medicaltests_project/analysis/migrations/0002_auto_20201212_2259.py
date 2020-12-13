# Generated by Django 3.1.4 on 2020-12-12 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20201212_2259'),
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicaltest',
            name='patientID',
        ),
        migrations.AddField(
            model_name='medicaltest',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='authentication.patient'),
            preserve_default=False,
        ),
    ]