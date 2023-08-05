<h1 align="center">Chat With RC4 Cript</h1>

<p align="center">Chat com encriptação RC4</p>

<hr> 

### :hammer_and_wrench: Tecnologias e Conceitos:

* Python 3.11

<div align="center" style="display: inline_block">
	<img src="https://img.shields.io/static/v1?label=Python&message=v3.11&color=3572A5&style=flat"/>
	<img src="https://img.shields.io/static/v1?label=license&message=MIT&color=green&style=flat"/>
</div>

### :gear: Configurações:

* Iniciar o servidor:
```bash
docker build -f python.Dockerfile -t build-amb ./ && docker run --rm -it --entrypoint bash -v ${PWD}:/app build-amb 
python server.py
```
* Rodar o docker:
```bash
docker build -f python.Dockerfile -t build-amb ./ && docker run --rm -it --entrypoint bash -v ${PWD}:/app build-amb 
```
* Executar o comando:
```bash
python client.py
```

### :warning: Erros/Aprimoramentos:

* Ao tentar iniciar o client.py, resulta em erro 
	* Obs 1: Algumas soluções indicam "xhost +", mas é inseguro por questão de acesso, assim deveria ser "xhost +local:docker". Entretanto nem com isso funcionou
* Melhorar código/estrutura do projeto
* Transferir para inglês(?)

##

<div align="center">
	<p>Feito com :computer: + :heart: por Leonardo Junio</p>
</div>
