def calculate_wallpaper(area, roll_width=1.06, roll_length=10, price_per_roll=2953):
    """
    Рассчитывает количество рулонов обоев и стоимость
    """
    perimeter = area ** 0.5 * 4  # Упрощённый расчёт периметра
    strips = perimeter / roll_width
    rolls = strips / (roll_length / 3)  # 3м высота комнаты
    rolls = int(rolls) + 1
    total_cost = rolls * price_per_roll
    return rolls, total_cost