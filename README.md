# Конспекти з курсу Автоматизація та КТ

В даному репозиторії зібрані вихідні файли конспектів.

## Предмети

- [Автоматизація ТП та виробництв (2 курс)](automation-tp-and-manufacuring)
  [[PDF](automation-tp-and-manufacuring/build/build.pdf)]
- [Стандартизація взаємозамінність систем та управління якістю (2 курс)](si-and-qm)
  [[PDF](si-and-qm/build/build.pdf)]
- [Соціологія (2 курс)](sociology)
  [[PDF](sociology/build/build.pdf)]
- [Політологія (2 курс)](politology)
  [[PDF](politology/build/build.pdf)]

[Зворотній зв’язок.](mailto:linevich.net@gmail.com)

## Інструкції по збірці PDF [TODO]

Процес розрахований на збирання під Linux і під Windows не перевірявся. Всі дії виконуються
в Debian, але і для Ubuntu інструкція має підійти.

Для початку потрібно
[завантажити і встановити Pandoc](https://github.com/jgm/pandoc/releases/latest).

Також для збірки потрібен xelatex:

```
sudo apt-get install texlive-full texlive-xetex -y
```

Після задоволення всіх залежностей достатньо перейти в папку з конспектом і виконати в ній команду
`make pdf`, і ви отримаєте готовий PDF який буде знаходитись за таким шляхом:
`назва_конспекту/build/build.pdf`
