# Generated by Django 3.0.8 on 2020-07-15 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=200)),
                ('longitude', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1300)),
                ('img_path', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('PHONE', 'Phone'), ('FACEBOOK', 'Facebook'), ('EMAIL', 'Email')], default='EMAIL', max_length=10)),
                ('value', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('logo', models.CharField(max_length=120)),
                ('branches', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Branch')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courses', to='app.Category')),
                ('contacts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Contact')),
            ],
        ),
    ]
