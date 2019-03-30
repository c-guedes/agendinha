from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE,
    verbose_name="Usuário")
    nome = models.CharField("Nome", max_length = 128)
    data_de_nascimento = models.DateField(
        'Data de nascimento', blank=True, null=True)
    telefone_celular = models.CharField("Telefone celular", max_length=15,
    help_text = 'Número do telefone celular no formato (99) 99999-9999',
    null=True, blank=True)
    telefone_fixo = models.CharField("Telefone fixo", max_length=15,
    help_text = 'Número do telefone celular no formato (99) 99999-9999',
    null=True, blank=True)
    email = models.EmailField('E-mail',null=True,blank=True)

    def __str__(self):
        return self.nome

 
class Compromisso(models.Model):
    criadorCompromisso = models.ForeignKey(Pessoa, on_delete=models.CASCADE, blank=True, null = True)
    nomeCompromisso = models.CharField("Nome Compromisso", max_length = 128)
    dataOcorre = models.DateField(
            'Data do compromisso', blank=True, null=True)
    horaOcorre = models.DateTimeField('Hora do compromisso', blank=True, null=True)
    def __str__(self):
        return self.nomeCompromisso

class AgendaInstitucional(models.Model):
    class Meta:
        verbose_name = "Agenda Institucional"
    compromisso = models.ManyToManyField(Compromisso)
    ano = models.CharField("Ano Institucional", max_length=128)
    def __str__(self):
        return self.ano

class Agenda(models.Model):
    class Meta:
        verbose_name = "Agenda"
        verbose_name_plural = "Agendas"
    donoAgenda = models.ForeignKey(Pessoa, on_delete=models.CASCADE, blank=True, null = True)
    compromisso = models.ManyToManyField(Compromisso)
    agendaInstitucional = models.ForeignKey(AgendaInstitucional, on_delete=models.CASCADE, blank=True, null = True)
    privada = models.BooleanField("Agenda Pública?", blank=True, null = True)