# Generated by Django 5.0.6 on 2024-06-14 06:43

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GovChat_core', '0014_remove_chathistory_selected_files'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessUnit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=64, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='user',
            name='business_unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='GovChat_core.businessunit'),
        ),
        migrations.AddField(
            model_name='user',
            name='grade',
            field=models.CharField(choices=[('AA', 'AA'), ('AO', 'AO'), ('DD', 'Deputy Director'), ('D', 'Director'), ('DG', 'Director General'), ('EO', 'EO'), ('G6', 'G6'), ('G7', 'G7'), ('HEO', 'HEO'), ('PS', 'Permanent Secretary'), ('SEO', 'SEO'), ('OT', 'Other')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='profession',
            field=models.CharField(choices=[('AN', 'Analysis'), ('CMC', 'Commercial'), ('COM', 'Communications'), ('CFIN', 'Corporate finance'), ('CF', 'Counter fraud'), ('DDT', 'Digital, data and technology'), ('EC', 'Economics'), ('FIN', 'Finance'), ('FEDG', 'Fraud, error, debts and grants'), ('HR', 'Human resources'), ('IA', 'Intelligence analysis'), ('IAUD', 'Internal audit'), ('IT', 'International trade'), ('KIM', 'Knowledge and information management'), ('LG', 'Legal'), ('MD', 'Medical'), ('OP', 'Occupational psychology'), ('OD', 'Operational delivery'), ('OR', 'Operational research'), ('PL', 'Planning'), ('PI', 'Planning inspection'), ('POL', 'Policy'), ('PD', 'Project delivery'), ('PR', 'Property'), ('SE', 'Science and engineering'), ('SC', 'Security'), ('SR', 'Social research'), ('ST', 'Statistics'), ('TX', 'Tax'), ('VET', 'Veterinary'), ('OT', 'Other')], max_length=4, null=True),
        ),
    ]
