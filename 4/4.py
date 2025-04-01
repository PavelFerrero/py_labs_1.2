import asyncio
from functools import wraps

# Декоратор для асинхронного выполнения
def async_decorator(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        return await func(*args, **kwargs)
    return wrapper

# Замыкание для записи в файл с применением декоратора
@async_decorator
async def file_writer_closure(filename):
    async def write_to_file(value):
        with open(filename, 'a') as f:
            f.write(str(value) + '\n')
    return write_to_file

# Основная асинхронная функция
async def main():
    # Создаем экземпляр замыкания
    writer = await file_writer_closure('output.txt')
    
    # Записываем данные
    await writer("4ivauva")
    await writer(42)
    
    print("Данные записаны в файл 'output.txt' ")

# Запуск программы
if __name__ == "__main__":
    asyncio.run(main())
