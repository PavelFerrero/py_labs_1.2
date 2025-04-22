def calculate_laminate(area, pack_area=2, price_per_pack=3392):
    """
    Рассчитывает количество упаковок ламината и стоимость
    """
    packs = int(area / pack_area * 1.1) + 1  # +10% на отходы
    total_cost = packs * price_per_pack
    return packs, total_cost