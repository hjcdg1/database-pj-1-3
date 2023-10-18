FROM python:3.8

WORKDIR /app
COPY . /app
RUN pip install lark==1.1.7 berkeleydb==18.1.6
CMD ["tail", "-f", "/dev/null"]
