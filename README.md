# Dockerized Django Project

Це Dockerized Django проект з PostgreSQL як база даних. Проект включає конфігурації для Docker і Docker Compose для полегшення розробки та розгортання.

## Prerequisites

Переконайтеся, що у вас встановлено такі інструменти:
- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/)

## Getting Started

### Clone the Repository

Спочатку клонуйте репозиторій на локальну машину:

```bash
git clone https://github.com/ZaharAlex2004/lessons_ubuntu.git
```

Після цього перейдіть до директорії проекту:

```bash
cd Pro/l23/docker_project
```

### Configuring the .env File

Створіть файл .env в корені проекту. Цей файл містить всі конфігурації середовища (паролі, назви бази даних тощо).

### Starting the Project

Для запуску проєкта виконайте команду:
```bash
docker-compose up --build
```

Для запуску проєкта у фоновому режимі виконайте команду:

```bash
docker-compose up -d
```

### Running Migrations

Після того як контейнери будуть запущені, потрібно виконати міграції для налаштування бази даних. 
Для цього скористайтеся командою:

```bash
docker-compose exec web python manage.py migrate
```

### Create superuser

Для отримання доступу до адмінки Django потрібно створити суперкористувача. 
Виконайте команду:

```bash
docker-compose exec web python manage.py createsuperuser
```

### Accessing the Django App

Тепер ви можете відкрити ваш веб-браузер і перейти за адресою:

```bash
http://localhost:8000
```

або

```bash
http://0.0.0.0:8000
```

### Accessing Django Admin Panel

Посилання на перехід до адмінки:

```bash
http://localhost:8000/admin
```

або

```bash
http://0.0.0.0:8000/admin
```

### Stopping the Project

Для зупинки проєкту, виконайте команду:

```bash
docker-compose down
```

