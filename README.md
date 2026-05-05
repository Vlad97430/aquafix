# AquaFix — Сервіс сантехнічних послуг

## Стек технологій
- **Backend:** Django 6.0 + Django REST Framework
- **База даних:** PostgreSQL 15
- **Документація API:** drf-spectacular (Swagger UI)
- **Контейнеризація:** Docker + Docker Compose

## Запуск проекту

### 1. Клонування репозиторію
```bash
git clone https://github.com/Vlad97430/aquafix
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

### 5. Створення адміністратора
```bash
docker-compose exec backend python manage.py createsuperuser
```

## Перевірка працездатності
- Головна сторінка: http://localhost:8001
- Адмін панель: http://localhost:8001/admin
- Swagger UI: http://localhost:8001/api/swagger/
- ReDoc: http://localhost:8001/api/redoc/
- API Schema: http://localhost:8001/api/schema/

## Зупинка контейнерів
```bash
docker-compose down
```

## Приклади запитів

### 1. Отримати всі категорії
```bash
curl -X GET http://localhost:8001/api/categories/ \
  -H "accept: application/json"
```

### 2. Створити нову категорію
```bash
curl -X POST http://localhost:8001/api/categories/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Монтаж", "description": "Монтаж сантехніки", "is_active": true}'
```

### 3. Отримати активні послуги
```bash
curl -X GET http://localhost:8001/api/services/active/ \
  -H "accept: application/json"
```

### 4. Створити замовлення
```bash
curl -X POST http://localhost:8001/api/orders/ \
  -H "Content-Type: application/json" \
  -d '{"user": 1, "service": 1, "description": "Протікає кран", "address": "вул. Шевченка 1", "status": "new"}'
```

### 5. Отримати доступних співробітників
```bash
curl -X GET http://localhost:8001/api/employees/available/ \
  -H "accept: application/json"
```

## API Endpoints

| Ресурс | URL | Методи |
|--------|-----|--------|
| Категорії | /api/categories/ | GET, POST |
| Категорія | /api/categories/{id}/ | GET, PUT, PATCH, DELETE |
| Активні категорії | /api/categories/active/ | GET |
| Послуги | /api/services/ | GET, POST |
| Послуга | /api/services/{id}/ | GET, PUT, PATCH, DELETE |
| Активні послуги | /api/services/active/ | GET |
| Співробітники | /api/employees/ | GET, POST |
| Доступні | /api/employees/available/ | GET |
| Замовлення | /api/orders/ | GET, POST |
| За статусом | /api/orders/by-status/{status}/ | GET |
| Платежі | /api/payments/ | GET, POST |
| Відгуки | /api/reviews/ | GET, POST |
| Видимі відгуки | /api/reviews/visible/ | GET |
| Повідомлення | /api/messages/ | GET, POST |
| Непрочитані | /api/messages/unread/ | GET |
| Користувачі | /api/users/ | GET, POST |