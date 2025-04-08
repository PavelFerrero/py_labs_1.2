# Отчёт по лабораторной работе №5: Генераторы

## Условие задачи  
**Задача 9:** Создать полископный генератор для растровых изображений, который инвертирует цвета пикселей. К генератору должна быть применена хотя бы одна из функций `map`, `reduce`, `filter`.

---

## Описание проделанной работы  

### Цель  
Разработать генератор для инверсии цветов пикселей изображения с использованием функций высшего порядка (`map`, `reduce`, `filter`).  

### Принцип Работы
1. **Библиотеки:** Использован модуль `PIL` (Pillow) для работы с изображениями.
2. **Генератор `pikseli_generator`:**
   - Открывает изображение в режиме `RGBA` с сохранением прозрачности.
   - Последовательно возвращает кортежи `(x, y, (r, g, b, a))` для каждого пикселя через `yield`.
   - Позволяет обрабатывать изображение построчно без загрузки всех данных в память.
3. **Функция `invert_piksel`:**
   - Принимает данные пикселя в формате `(x, y, (r, g, b, a))`.
   - Инвертирует цветовые каналы RGB по формуле `(255 - r, 255 - g, 255 - b)`.
   - Сохраняет исходное значение альфа-канала без изменений.
4. **Применение `map`:**
   - Функция высшего порядка `map` применяет `invert_piksel` к каждому элементу генератора.
   - Создает итератор с инвертированными пикселями в формате `(x, y, inverted_color)`.
5. **Сохранение результата:**
   - Обработанные пиксели записываются обратно в изображение.
   - Производится конвертация в режим `RGB` для корректного отображения.
   - Результат сохраняется с сохранением исходного формата.

### Код  
```python
from PIL import Image

# Открываем изображение
izobrazhenie = Image.open("C:\Github_py\labs1.png").convert('RGBA')
pikseli = izobrazhenie.load()

shirina, vysota = izobrazhenie.size

# Генератор для перебора пикселей
def pikseli_generator(image_pixels, width, height):
    for x in range(width):
        for y in range(height):
            yield (x, y, image_pixels[x, y])  # (x, y, (r, g, b, a))

# Функция для инверсии цвета
def invert_piksel(piksel_data):
    x, y, (r, g, b, a) = piksel_data
    inverted_color = (255 - r, 255 - g, 255 - b, a)
    return x, y, inverted_color

# Применяем map к генератору
inverted_pixels = map(invert_piksel, pikseli_generator(pikseli, shirina, vysota))

# Записываем пиксели обратно в изображение
for x, y, inverted_color in inverted_pixels:
    pikseli[x, y] = inverted_color

# Принудительно конвертируем в RGB для корректного отображения
izobrazhenie = izobrazhenie.convert('RGB')

# Сохраняем результат
izobrazhenie.save("C:\Github_py\labs1.png")

print("Инверсия завершена! Сохранено как output.png")

```

###  Изображение ДО:

![image](https://github.com/user-attachments/assets/4486d99e-8be4-4ceb-af16-5981236d6b63)

### Изображение ПОСЛЕ:

![image](https://github.com/user-attachments/assets/8cda6d54-5aa7-4517-ac1f-79cb27b578b3)



### Источники:

[Pillow](https://python-scripts.com/pillow?ysclid=m9826lcsz7721883869)

[Генераторы в Python](https://habr.com/ru/articles/866616/)

[map в Puthon](https://skillbox.ru/media/code/funkciya-map-v-python-zachem-nuzhna-i-kak-ey-polzovatsya/?ysclid=m984sk6958411790248)
