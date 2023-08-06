# Imagem de Origem
FROM python:3

# requirements.txt gerado por python -m pip freeze > requirements.txt
#(Ignorado por enquanto)Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. 
#It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt

RUN apt-get update && apt-get install x11-xserver-utils -y  

COPY . /app

# Diretório de trabalho(é onde a aplicação ficará dentro do container).
WORKDIR /app

#USER 1000

# docker build -f python.Dockerfile -t build-amb ./ && docker run --rm -it --entrypoint bash -v ${PWD}:/app build-amb 
# docker rmi build-amb
