# Generated by Django 4.2.4 on 2023-12-05 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("lees_app", "0003_remove_student_first_name_remove_student_last_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="dept",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="lees_app.department",
            ),
        ),
    ]
