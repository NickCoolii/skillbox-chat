# SkillBox - Приложение мини-чат на Python

В данном репозитории находятся материалы и примеры кода с 
[онлайн интенсива](https://webinar.skillbox.ru/messenger-python/) по разработке на Python от [SkillBox](https://skillbox.ru) 

## Установка

Для установки зависимостей проекта необходимо выполнить

```
pip install -r requirements.txt
```

Для просмотра списка установленных пакетов

```
pip list
```

Для выгрузки списка установленных пакетов

```
pip freeze > requirements.txt
```

Для установки Telnet

MacOS:
```
brew install telnet
```

Ubuntu:
```
sudo apt-get install telnet
```

Windows: [инструкция](https://help.keenetic.com/hc/ru/articles/213965809-%D0%92%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-%D1%81%D0%BB%D1%83%D0%B6%D0%B1-Telnet-%D0%B8-TFTP-%D0%B2-Windows)

## Возможные проблемы

### Проблема установки библиотек twisted/PyQt5-sip в PyCharm (Windows)

- Необходимо установить С++ build tools
    - [Объяснение](https://stackoverflow.com/a/40525033/4941870)
    - [Качать отсюда](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019) "Build Tools for Visual Studio 2019"
    - Установить.
    - Перезагрузить компьютер
    - Повторить установку пакетов `pip install -r requirements.txt`

(за вклад спасибо [NickCoolii](https://github.com/NickCoolii))

## Структура репозитория

- **basic** - примеры кода с вебинаров
    - **first** - первый день, работа с данными, синтаксис и операции, начало ООП
    - **second** - примеры ООП, работа с сетью, библиотека Twisted 
    - **third** - примеры интерфейса на Qt
- **examples** - дополнительные примеры программ и материалы с вебинара
- **src** - готовый проект мини-чата

## Полезные книги

- Программирование на Python (Марк Лутц - O'Reilly)
- Простой Python. Современный стиль программирования (Любанович Билл - O'Reilly)
- Python. Карманный справочник (Марк Лутц - O'Reilly)
- Изучение сложных систем с помощью Python (Аллен Б. Дауни - O'Reilly)
- Приемы объектно-ориентированного проектирования. Паттерны проектирования (Гамма Эрих, Джонсон Р., Хелм Ричард, Влиссидес Джон - Питер)
- Совершенный код. Мастер-класс (Стив Макконнелл - БХВ-Петербург)
