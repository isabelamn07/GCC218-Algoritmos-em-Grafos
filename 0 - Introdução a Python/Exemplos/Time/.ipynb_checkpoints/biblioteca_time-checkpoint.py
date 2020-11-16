
'''
Código      Descrição
%a          dia da semana abreviado
%A          nome do dia da semana
%b          nome do mês abreviado
%B          nome do mês completo
%c          data e hora conforme configuração regional
%d          dia do mês(01-31)
%H          hora no formato 24h(00-23)
%I          hora no formato 12h
%j          dia do ano 001 - 366
%m          mês(01-12)
%M          minutos(00-59)
%p          AM ou PM
%S          segundos(00-61)
%U          número da semana (00-53), onde a semana 1 começa após o primeiro domingo.
%w          dia da semana(0-6) onde é o domingo
%W          número da semana(00-53), onde a semana 1 começa após a primeira segunda-feira
%x          representação regional da data
%X          representação regional da hora
%y          ano(00-99)
%Y          ano com 4 dígitos
%Z          nome do fuso horário
%           símbolo de %

'''


from time import gmtime, strftime
print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))

# Fonte: Introdução à programação com Python : algoritmos e lógica de programação para iniciantes / Nilo Ney Coutinho Menezes. 