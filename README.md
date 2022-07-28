# Usando o executor de comando remoto

## Configurando ambiente

Primeiro, adicione um arquivo .env ou uma variável de ambiente chamada MONGODB_URI.
Este será o banco de dados usado para registrar as informações.
Vaso ache melhor, substitua no código fonte em /database/database.py a função de captura de variável pela URI.

Para instalar os pacotes usados, execute o comando:
```shell
pip3 install -r requirements.txt
```

## Compilando o projeto

Caso deseje ter um executável em mãos, pode optar por usar o pyinstaller, que já é instalado com as dependências do projeto.
Para compilar execute:
```shell
pyinstaller --onefile rsecli.py
```
Caso eseja em máquina linux, pode compilar o .deb com as instuções abaixo e instalar em seu computador

## Compilando em .deb

## Usando a cli

Para obter uma lista de todos os possíveis comandos, basta executar:
```shell
rsecli help
python3 rsecli.py help
```

A cli foi feitapara ser bem intuituva, mas não funciona sem o receiver, que se encontra [https://github.com/MarcoLopes389/rsecli-receiver](neste link)
