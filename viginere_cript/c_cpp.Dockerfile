FROM gcc:12.2

COPY . /app

WORKDIR /app

# Formas de rodar C ou C++, caso deseje que ao rodar o docker, ele já execute
# Inserir trecho no Run
#gcc program_source_code.c -o executable_file_name OR cc program_source_code.c -o executable_file_name
#g++ program_source_code.cpp -o executable_file_name
# assuming that executable_file_name.c ou executable_file_name.cpp exists
#make executable_file_name
#./executable_file_name

#RUN <forma_rodar_acima>

#CMD ["./executable_file_name"]



# docker build -f c_cpp.Dockerfile -t my-gcc-app ./ && docker run -it --rm my-gcc-app
