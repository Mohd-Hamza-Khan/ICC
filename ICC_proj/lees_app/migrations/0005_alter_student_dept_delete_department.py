# Generated by Django 4.2.4 on 2023-12-05 19:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lees_app", "0004_alter_student_dept"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="dept",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name="Department",
        ),
    ]
