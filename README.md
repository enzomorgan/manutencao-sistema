# Sistema de Gerenciamento do Condomínio

## Requisitos

- Python 3.x
- Django
- Django Rest Framework
- drf-spectacular

## Instruções de Instalação

#1. **Ative o ambiente virtual:**
Para garantir que você está trabalhando dentro do ambiente virtual do projeto, execute o seguinte comando no terminal: 
```bash 
.\venv\Scripts\activate
```
#2. **Atualize o pip:**
É uma boa prática garantir que o pip esteja atualizado. Execute o seguinte comando para atualizar o pip: 
```bash 
python.exe -m pip install --upgrade pip
``` 
#3. **Instale o Django:**
Se ainda não tiver o Django instalado, execute o comando abaixo para instalá-lo: 
```bash 
Instale o Django Rest Framework (DRF):
``` 
## O Django Rest Framework é utilizado para criar APIs de forma fácil e eficiente. Para instalá-lo, execute: 
```bash 
pip install djangorestframework
``` 
#4. **Instale o drf-spectacular:**

O drf-spectacular é uma ferramenta para gerar documentação automatizada para a API. Instale-a com o comando: 
```bash 
pip install drf-spectacular
```
#5. **Configuração do Projeto**
Após realizar a instalação das dependências, você pode configurar o projeto com as migrações do banco de dados: 
```bash 
python manage.py migrate
```
#6. **Inicie o Servidor de Desenvolvimento:**
Agora você pode rodar o servidor de desenvolvimento do Django com o comando: 
``` bash 
python manage.py runserver
```
