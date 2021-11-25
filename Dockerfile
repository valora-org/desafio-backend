FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /my_app_dir
WORKDIR /my_app_dir
ADD requirements.txt /my_app_dir/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /my_app_dir/