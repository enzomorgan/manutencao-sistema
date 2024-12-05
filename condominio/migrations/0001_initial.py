# condominio/migrations/0001_initial.py

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # Adicione as dependências, se houver
        # Exemplo: ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Condominio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=20, null=True, blank=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
