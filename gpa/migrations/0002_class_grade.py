# Generated by Django 3.0.2 on 2020-03-02 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='grade',
            field=models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('A-', 'A-'), ('B+', 'B+'), ('B', 'B'), ('B-', 'B-'), ('C+', 'C+'), ('C', 'C'), ('C-', 'C-'), ('D+', 'D+'), ('D', 'D'), ('D-', 'D-'), ('F+', 'F+')], default=' ', max_length=3),
        ),
    ]