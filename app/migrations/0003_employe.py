# Generated by Django 4.1.7 on 2023-04-07 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_department_deptno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('empno', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('MGR', models.CharField(max_length=100)),
                ('hiredate', models.DateField()),
                ('sal', models.IntegerField()),
                ('comm', models.IntegerField(blank=True)),
                ('deptno', models.IntegerField()),
            ],
        ),
    ]