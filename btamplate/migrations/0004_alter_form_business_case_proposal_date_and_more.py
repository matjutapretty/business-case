# Generated by Django 4.0.2 on 2022-03-15 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btamplate', '0003_alter_form_business_case_proposal_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='Business_case_proposal_date',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='form',
            name='Estimated_completion_Date',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='form',
            name='Overall_Project_Timeframe',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='form',
            name='Proposed_Start_Date',
            field=models.CharField(max_length=200),
        ),
    ]
