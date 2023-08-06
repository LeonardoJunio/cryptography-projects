<h1 align="center">Date Cript</h1>

<p align="center">Encripta e desencripta o conteudo de um texto de acordo com uma data dita pelo usuário</p>

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

### :warning: Erros/Aprimoramentos:

* Está ocorrendo alguns erros quando se tentar encriptar/descriptar, talvez devido as caracteres especiais ou alguma configuração no docker
* Melhorar código/estrutura do projeto
* Transferir para inglês(?)

##

<div align="center">
	<p>Feito com :computer: + :heart: por Leonardo Junio</p>
</div>
