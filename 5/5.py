
from PIL import Image

# Открываем изображение
izobrazhenie = Image.open("C:\Github_py\labs.png").convert('RGBA')
pikseli = izobrazhenie.load()

shirina, vysota = izobrazhenie.size

# Генератор для инверсии пикселей
def invert_pikseli(image_pixels, width, height):
    for x in range(width):
        for y in range(height):
            r, g, b, a = image_pixels[x, y]
            inverted = (255 - r, 255 - g, 255 - b, a)  # инвертируем только RGB
            yield x, y, inverted

# Применяем изменения
for x, y, inverted_color in invert_pikseli(pikseli, shirina, vysota):
    pikseli[x, y] = inverted_color

# Принудительно конвертируем в RGB для корректного отображения
izobrazhenie = izobrazhenie.convert('RGB')

# Сохраняем результат
izobrazhenie.save("C:\Github_py\labs.png")

print("Инверсия завершена! Сохранено как output.png")
