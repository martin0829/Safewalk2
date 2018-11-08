# Generated by Django 2.1.3 on 2018-11-08 03:14

from django.db import migrations, models
import django.db.models.deletion
import main.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departTime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('long', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Walker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True, validators=[main.validators.validate_email])),
                ('photo', models.ImageField(upload_to='walkers/profile/')),
                ('rating', models.IntegerField()),
                ('emgContact', models.CharField(max_length=200)),
                ('party', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.Party')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='party',
            name='endLoc',
            field=models.ManyToManyField(related_name='end', to='main.Region'),
        ),
        migrations.AddField(
            model_name='party',
            name='startLoc',
            field=models.ManyToManyField(related_name='start', to='main.Region'),
        ),
    ]
