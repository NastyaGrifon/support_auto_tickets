# Тестовое задание

## Описание

Скрипт умеет вот что:

1.  Подсчитывает количество нерешённых тикетов и выводит их список.
2.  Подсчитывает количество тикетов в каждой категории.
3.  Записывает результаты в файл с автоматически сгенерированным уникальным именем.

## Требования

-   Python 3.6 или выше

## Использование

### Запуск, отчёт создаётся в текущую директорию

`python3 tickets.py`

### Для запуска каждые три часа с записью **в домашнюю директорию текущего пользователя**

`crontab -e`

`0 */3 * * * python3 /path/to/script/tickets.py`

### Для запуска каждые три часа с записью **в произвольную директорию**

`crontab -e`

`0 */3 * * * cd /report/path/ && python3 /path/to/script/tickets.py`


