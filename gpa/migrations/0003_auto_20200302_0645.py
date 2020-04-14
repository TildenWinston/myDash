# Generated by Django 3.0.2 on 2020-03-02 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpa', '0002_class_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='GPA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GPA', models.FloatField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='credit_hours',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='class',
            name='semester',
            field=models.CharField(choices=[('FALL', 'Fall'), ('SPRING', 'Spring'), ('SUMMER', 'Summer Session'), ('JANUARY', 'J-Term')], default=' ', max_length=20),
        ),
        migrations.AddField(
            model_name='class',
            name='year',
            field=models.FloatField(default=0),
        ),
    ]