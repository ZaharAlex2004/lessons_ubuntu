FROM python:3.12

RUN useradd -m ALEX

WORKDIR /l23

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

USER root

COPY . /l23

RUN mkdir -p /l23/docker_project/staticfiles /l23/docker_project/media \
    && chown -R ALEX:ALEX /l23/docker_project/staticfiles /l23/docker_project/media

CMD ["python", "docker_project/manage.py", "runserver", "0.0.0.0:8000"]
