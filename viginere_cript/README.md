<h1 align="center">Viginere Cript</h1>

<p align="center">Desencripta o conteudo de um texto de acordo com uma chave informada</p>

<hr> 

### :hammer_and_wrench: Tecnologias e Conceitos:

* C (gcc 12.2 / make 4.3) 

<div align="center" style="display: inline_block">
	<img src="https://img.shields.io/static/v1?label=C&message=v12.2&color=555555&style=flat"/>
	<img src="https://img.shields.io/static/v1?label=license&message=MIT&color=green&style=flat"/>
</div>

### :gear: Configurações:

* Rodar o docker:
```bash
docker build -f c_cpp.Dockerfile -t my-gcc-app ./ && docker run -it --rm my-gcc-app
```
* Executar o comando:
```bash
make main **OR** gcc main.c -o main 
./main 
```
* Dentre as opções exibidas, escolher o conteúdo e chave referente á aquele conteúdo (atualmente são: segredo; Despacito)

### :warning: Erros/Aprimoramentos:

* Seria interessante ter uma opção para encriptar e não só criptografar
* Melhorar código/estrutura do projeto
* Transferir para inglês(?)

##

<div align="center">
	<p>Feito com :computer: + :heart: por Leonardo Junio</p>
</div>
