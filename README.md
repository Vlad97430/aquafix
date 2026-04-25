# AquaFix — Сервіс сантехнічних послуг

## Стек технологій
- **Backend:** Django 6.0 + Django REST Framework
- **База даних:** PostgreSQL 15
- **Контейнеризація:** Docker + Docker Compose

## Запуск проекту

### 1. Клонування репозиторію
```bash
git clone <url>
cd aquafix
```

### 2. Створення .env файлу
```bash
cp .env.example .env
```

### 3. Запуск контейнерів
```bash
docker-compose up -d --build
```

### 4. Виконання міграцій
```bash
docker-compose exec backend python manage.py migrate
```

### 5. Перевірка працездатності
Відкрий браузер: http://localhost:8001

## Зупинка контейнерів
```bash
docker-compose down
```

## Перевірка що дані не зникають після перезапуску
```bash
docker-compose down
docker-compose up -d
```
Дані зберігаються завдяки volume `postgres_data`.