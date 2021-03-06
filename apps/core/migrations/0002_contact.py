# Generated by Django 3.2 on 2022-02-15 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('subject', models.CharField(max_length=128, verbose_name='Assunto')),
                ('message', models.TextField(verbose_name='Mensagem')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de envio')),
                ('is_answered', models.BooleanField(default=False, verbose_name='Mensagem Respondida?')),
                ('person_responsible', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Pessoa Responśavel')),
            ],
            options={
                'verbose_name': 'Contato',
                'verbose_name_plural': 'Contatos',
            },
        ),
    ]
