###Інструкція

Склонуйте репозиторій на локальну машину:
```bash
git clone https://github.com/ZaharAlex2004/lessons_ubuntu.git
```

Після цього перейдіть до директорії проекту:

```bash
cd Pro/l24/celery_project
```

### Configuring the .env File

Створіть файл .env в корені проекту. Цей файл містить всі конфігурації середовища (паролі, назви бази даних тощо).

### Starting the Project

Для запуску проєкта виконайте комади:
```bash
celery -A base flower
celery -A base beat --loglevel=info
celery -A base worker --loglevel=info
```
