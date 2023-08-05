<h1 align="center">Hash Cript</h1>

<p align="center">Encripta e desencripta os conteudos com base em Hash, além de verificar se o que foi gerado foi modificado</p>

<hr> 

### :hammer_and_wrench: Tecnologias e Conceitos:

* Python 3.11

<div align="center" style="display: inline_block">
	<img src="https://img.shields.io/static/v1?label=Python&message=v3.11&color=3572A5&style=flat"/>
	<img src="https://img.shields.io/static/v1?label=license&message=MIT&color=green&style=flat"/>
</div>

### :gear: Configurações:

* Rodar o docker:
```bash
docker build -f python.Dockerfile -t build-amb ./ && docker run --rm -it --entrypoint bash -v ${PWD}:/app build-amb 
```
* Executar o comando:
```bash
cd App/
python main.py
```

### :warning: Erros/Aprimoramentos:

* Melhorar código/estrutura do projeto
* Utilizar uma pasta separada para armazenar os textos e ajustar no codigo para manipular somente os conteudos desta
* Ajustar Dockerfile para pegar os conteudos somente da pasta App
* Transferir para inglês(?)

##

<div align="center">
	<p>Feito com :computer: + :heart: por Leonardo Junio</p>
</div>
