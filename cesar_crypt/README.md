<h1 align="center">Cesar Crypt</h1>

<p align="center">Decrypts the content of a text according to the key chosen by the user</p>

<hr> 

### :hammer_and_wrench: Technologies & Concepts:

* C 12.2

<div align="center" style="display: inline_block">
	<img src="https://img.shields.io/static/v1?label=C&message=v12.2&color=555555&style=flat"/>
	<img src="https://img.shields.io/static/v1?label=license&message=MIT&color=green&style=flat"/>
</div>

### :gear: Settings:

* Launch dockerfile:
```bash
docker build -f c_cpp.Dockerfile -t my-gcc-app ./ && docker run -it --rm -v ./:/app my-gcc-app
```

* Run the following commands:
```bash
cd cesar_crypt/
make
./bin/app 
```

### :warning: Bugs/Improvements:

* It would be interesting to have an option to encrypt, with a numeric key said by the user

##

<div align="center">
	<p>Made with :computer: + :heart: by Leonardo Junio</p>
</div>
