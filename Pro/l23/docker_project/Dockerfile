FROM python:3.12

RUN useradd -m ALEX

WORKDIR /l23

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

USER ALEX

COPY . /l23

CMD ["python", "docker_project/manage.py", "runserver", "http://localhost:8000"]

RUN pip install --no-cache-dir --root-user-action=ignore -r requirements.txt
