def calculate_tile(area, tile_size=0.3, price_per_pack=3871, tiles_per_pack=10):
    """
    Рассчитывает количество плитки и стоимость
    """
    tile_area = tile_size ** 2
    tiles_needed = area / tile_area * 1.1  # +10% на подрезку
    packs = int(tiles_needed / tiles_per_pack) + 1
    total_cost = packs * price_per_pack
    return packs, total_cost