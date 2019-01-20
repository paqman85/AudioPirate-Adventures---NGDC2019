# Generated by Django 2.1.5 on 2019-01-20 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googlepirate', '0002_auto_20190119_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='DialogFlowData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responseId', models.CharField(max_length=600)),
                ('queryText', models.CharField(max_length=600)),
                ('parameters', models.CharField(blank=True, max_length=600, null=True)),
                ('allRequiredParamsPresent', models.BooleanField()),
                ('fulfillmentText', models.CharField(blank=True, max_length=600, null=True)),
                ('fulfillmentMessages', models.CharField(blank=True, max_length=600, null=True)),
                ('ACTIONS_ON_GOOGLE', models.CharField(blank=True, max_length=600, null=True)),
                ('textToSpeech', models.CharField(blank=True, max_length=600, null=True)),
                ('displayText', models.CharField(blank=True, max_length=600, null=True)),
                ('intentname', models.CharField(blank=True, max_length=600, null=True)),
                ('displayName', models.CharField(blank=True, max_length=600, null=True)),
                ('intentDetectionConfidence', models.CharField(blank=True, max_length=50, null=True)),
                ('languageCode', models.CharField(blank=True, max_length=50, null=True)),
                ('originalDetectIntentRequest', models.CharField(blank=True, max_length=600, null=True)),
                ('session', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='UserSessionData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=300)),
                ('loottotal', models.IntegerField()),
                ('crewtotal', models.IntegerField()),
                ('reknown', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='randomencounterssea',
            name='num',
            field=models.CharField(max_length=100),
        ),
    ]