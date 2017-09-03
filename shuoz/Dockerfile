FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV LANG zh_CN.UTF-8
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app/
ADD requirements.txt /usr/src/app/
RUN pip3 install -r requirements.txt -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/
