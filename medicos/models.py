from django.db import models
from django.core.validators import RegexValidator
from django.db.models.fields.related import ForeignKey


class Especialidade(models.Model):

    nome = models.CharField(verbose_name='Nome', max_length=200)
    descricao = models.CharField(verbose_name='Descrição', max_length=1000)
    
    def __str__(self):
        return f'{self.nome}'


class Medico(models.Model):

    val_telefone = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="O número precisa estar neste formato: \
                    '+XX XX XXXX-XXXX'."
    )

    nome = models.CharField(verbose_name='Nome', max_length=200)
    endereco = models.CharField(verbose_name='Endereço', max_length=200)
    crm = models.CharField(verbose_name='CRM', max_length=200)
    telefone = models.CharField(verbose_name='Telefone', validators=[val_telefone], max_length=17, null=True, blank=True)
    email = models.EmailField(verbose_name='Email')
    data_nascimento =models.DateField(verbose_name='Data de Nacimento')
    especialidade = ForeignKey(Especialidade, on_delete=models.CASCADE, related_name='medicos')

    def __str__(self):
        return f'{self.nome}'
    
