from instapy_cli import client

username = str(input('Usuário: '))
password = str(input('Senha: '))
image = str(input('Caminho da foto: '))
text = str(input('Texto: '))

with client(username, password) as cli:
    cli.upload(image, text)