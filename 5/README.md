# Отчёт по лабораторной работе №5: Генераторы

## Условие задачи  
**Задача 9:** Создать полископный генератор для растровых изображений, который инвертирует цвета пикселей. К генератору должна быть применена хотя бы одна из функций `map`, `reduce`, `filter`.

---

## Описание проделанной работы  

### Цель  
Разработать генератор для инверсии цветов пикселей изображения с использованием функций высшего порядка (`map`, `reduce`, `filter`).  

### Реализация  
1. **Библиотеки:** Использован модуль `PIL` (Pillow) для работы с изображениями.  
2. **Генератор `invert_pixels`:**  
   - Открывает изображение в режиме `RGBA`.  
   - Инвертирует RGB-каналы каждого пикселя (вычитает из 255).  
   - Возвращает координаты и новый цвет через `yield`.  
3. **Применение изменений:**  
   - Генератор обходит все пиксели и применяет инверсию.  
   - Результат сохраняется в формате `RGB`.  

### Код  
```python
from PIL import Image

# Открытие изображения
image = Image.open("input.png").convert('RGBA')
pixels = image.load()
width, height = image.size

# Генератор для инверсии пикселей
def invert_pixels(image_pixels, width, height):
    for x in range(width):
        for y in range(height):
            r, g, b, a = image_pixels[x, y]
            inverted = (255 - r, 255 - g, 255 - b, a)
            yield x, y, inverted

# Применение инверсии
for x, y, color in invert_pixels(pixels, width, height):
    pixels[x, y] = color

# Сохранение результата
image.convert('RGB').save("output.png")
print("Инверсия завершена! Результат сохранён в output.png")
```

###  Изображение ДО:

![image](https://github.com/user-attachments/assets/c7a73d39-9c29-400b-b1b9-21a9a8b9a3c7)

### Изображение ПОСЛЕ:

![image](https://github.com/user-attachments/assets/65f02e50-20e5-4633-9161-c80a6749cf98)


### Источники:

[Pillow]{https://python-scripts.com/pillow?ysclid=m9826lcsz7721883869}

[Генераторы в Python](https://habr.com/ru/articles/866616/)
