# Generated by Django 2.0.4 on 2018-08-16 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActionRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_data_time', models.DateTimeField(auto_now_add=True, verbose_name='action_data_time')),
                ('action_assigner', models.CharField(max_length=64, verbose_name='action_assigner')),
                ('action_reference', models.CharField(blank=True, max_length=64, null=True, verbose_name='action_reference')),
                ('action_record', models.CharField(blank=True, max_length=128, null=True, verbose_name='action_record')),
            ],
            options={
                'verbose_name_plural': 'action_record',
                'db_table': 'boss_action_record',
                'ordering': ['-action_data_time'],
                'verbose_name': 'action_record',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_data_time', models.DateTimeField(auto_now_add=True, verbose_name='log_data_time')),
                ('log_assigner', models.CharField(max_length=64, verbose_name='log_assigner')),
                ('log_reference', models.CharField(blank=True, max_length=64, null=True, verbose_name='log_reference')),
                ('log_record', models.CharField(blank=True, max_length=128, null=True, verbose_name='log_record')),
            ],
            options={
                'verbose_name_plural': 'log',
                'db_table': 'boss_log',
                'ordering': ['-log_data_time'],
                'verbose_name': 'log',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_data_time', models.DateTimeField(auto_now_add=True, verbose_name='message_data_time')),
                ('message_assigner', models.CharField(max_length=64, verbose_name='message_assigner')),
                ('message_reference', models.CharField(blank=True, max_length=64, null=True, verbose_name='message_reference')),
                ('message_record', models.CharField(blank=True, max_length=128, null=True, verbose_name='message_record')),
            ],
            options={
                'verbose_name_plural': 'message',
                'db_table': 'boss_message',
                'ordering': ['-message_data_time'],
                'verbose_name': 'message',
            },
        ),
    ]
