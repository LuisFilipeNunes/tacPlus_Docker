
# imagem base 
FROM ubuntu:bionic

# Atualiza a imagem e instala pacotes necessários e desinstala desnecessários. 

RUN apt-get update && \
    apt install -y tacacs+ && \
    apt-get clean

# Aponta a porta 49 
EXPOSE 49

ENV DEBUGLEVEL=32

#ENTRYPOINT Comando para inicializar o servidor TACACS+ 
ENTRYPOINT /usr/sbin/tac_plus -G -t -d ${DEBUGLEVEL} -C /etc/tacacs+/tac_plus.conf

# Comando para construir a imagem:
#       docker build --no-cache -t tacplus . 
# --no-cache > ignora camadas em cachê durante o processo de construcao

#Comando para execução. Aponta para o tac_plus.conf que está junto do Dockerfile, podendo ser atualizado conforme necessidade.
#Necessário apontar o caminho correto caso utilize outro arquivo. 
# $(pwd) aponta para o caminho atual do arquivo em execução. 

# docker run -td --name tacplus -p 49:49 -e DEBUGLEVEL=64 \
#       -v $(pwd)/tac_plus.conf:/etc/tacacs+/tac_plus.conf \
#       tacplus
