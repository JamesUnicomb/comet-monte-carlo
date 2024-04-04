FROM ubuntu:22.04

RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y python3 python3-dev python3-pip

RUN wget https://sourceforge.net/projects/gmat/files/GMAT/GMAT-R2022a/gmat-ubuntu-x64-R2022a.tar.gz
RUN tar -xvzf gmat-ubuntu-x64-R2022a.tar.gz

RUN cd GMAT/R2022a/api && python3 BuildApiStartupFile.py
RUN sed -i "s/<TopLevelGMATFolder>/\/GMAT\/R2022a/g" /GMAT/R2022a/api/load_gmat.py

COPY src/* ./