def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_cap = seed_type.capitalize()
    if seed_cap == "Tomato" or seed_cap == "Carrot" or seed_cap == "Lettuce":
        print(seed_cap + " seeds: ", end="")
    if unit == "area":
        print("covers", quantity, "square meters")
    elif unit == "packets":
        print(quantity, end="")
        print(" packets available")
    elif unit == "grams":
        print(quantity, end="")
        print(" grams total")
    else:
        print("Unknown unit type")
