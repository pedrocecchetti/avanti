from django.db import models


class Contact(models.Model):
    """
    Class that represents a contact that came from webForm
    """

    name = models.CharField(verbose_name='Nome', max_length=128, null=False, blank=False)
    email = models.EmailField(verbose_name='E-mail', null=False, blank=False)
    subject = models.CharField(verbose_name='Assunto', max_length=128, null=False, blank=False)
    message = models.TextField(verbose_name='Mensagem',null=False, blank=False)

    created_at = models.DateTimeField(verbose_name='Data de envio', auto_now_add=True)
    person_responsible = models.ForeignKey(verbose_name='Pessoa Responśavel',to='User', on_delete=models.SET_NULL, null=True)
    is_answered = models.BooleanField(verbose_name='Mensagem Respondida?', default=False)

    def __str__(self):
        return f'Mensagem de: {self.email} - {self.created_at}'

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'