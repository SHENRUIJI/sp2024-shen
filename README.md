# Проект Weather App

Этот проект включает в себя бэкенд и фронтенд для приложения, которое собирает данные о погоде из API OpenWeather и отображает их.

## Структура проекта

1. **Result_images**
   - В этой папке находятся результаты успешного выполнения.

2. **backend**
   - В этой папке находится код для бэкенда.
     - **app.py**: Этот файл Python содержит код бэкенда, который использует API OpenWeather для получения данных о погоде в Санкт-Петербурге.

3. **frontend**
   - В этой папке находится код для фронтенда.

4. **docker-compose.yaml**
   - Этот файл является файлом Docker Compose, который описывает сервисы и их конфигурации.

## Запуск проекта

### Предварительные требования

- Установлен Docker
- Установлен Docker Compose

### Шаги для запуска

1. **Сборка и запуск Docker контейнеров**
   ```sh
   docker-compose up --build
