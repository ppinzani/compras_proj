# compras_proj
Parte de compras del proyecto

Python Version: 3.4.3
Django Version: 1.8.10
Versiones mas detallas de los otros paquetes estan en el requirements.txt

Instrucciones para descargar python, pip, virtualenv, etc: https://ultimatedjango.com/learn-django/lessons/chapter-intro-3/
Para instalar la DB pip install psycopg2 (Habría que instalar tambien el pgadmin en linux)
Configurar la DB: https://ultimatedjango.com/learn-django/lessons/configure-the-database/?trim=yes (la parte del setting file ya esta hecha)

Habria que setear estas variables de entorno (yo lo agregue al .bashrc)
export ENV_ROLE="development"
export COMPRAS_DB_PASS=(Aca pones el pass de la DB)
export COMPRAS_SECRET_KEY="+mx#t3ymr)-c(fiagn#vubj+i*s6ju^t9@(-^p!bqk@lj@4hmo"

Instalar dj-static y short UUID: 
pip install dj-static
pip install django-shortuuidfield


