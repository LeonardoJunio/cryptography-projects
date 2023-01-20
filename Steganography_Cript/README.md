<h1 align="center">Steganography Cript</h1>

<p align="center">Encripta e desencripta o conteudo em uma imagem por meio de esteganografia (estudo e uso de técnicas para ocultar a existência de uma mensagem dentro de outra)</p>

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
* Obs: Os arquivos que são gerados pelo execução do programa, foi adicionado '\_' para evitar conflitos
* Executar o comando:
```bash
python main.py
```

### :warning: Erros/Aprimoramentos:

* Melhorar código/estrutura do projeto
* Ver forma de gerar outras imagens compativeis
* Transferir para inglês(?)

##

<div align="center">
	<p>Feito com :computer: + :heart: por Leonardo Junio</p>
</div>
