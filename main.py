
def dish_fetch(num):
    dishes = {
        1: {
            "id": 1,
            "name": "Bandeja paisa",
            "origin": "Antioquia",
            "ingredients": ["Frijoles", "Arroz", "Carne", "Huevo"]
        },
        2: {
            "id": 2,
            "name": "Arepa de huevo",
            "origin": "Costa Caribe",
            "ingredients": ["Maiz", "Huevo", "Sal"]
        },
        3: {
            "id": 3,
            "name": "Ajiaco",
            "origin": "Bogota",
            "ingredients": ["Pollo", "Papa", "Mazorca", "Guascas"]
        },
        4: {
            "id": 4,
            "name": "Sancocho",
            "origin": "Colombia",
            "ingredients": ["Yuca", "Platano", "Papa", "Carne"]
        },
        5: {
            "id": 5,
            "name": "Arroz con coco",
            "origin": "Costa Caribe",
            "ingredients": ["Arroz", "Coco", "Sal", "Azucar"]
        }
    }

    return dishes.get(num, {})


def main():
    print("=== MENU DE PLATOS COLOMBIANOS ===")
    print("1. Bandeja paisa")
    print("2. Arepa de huevo")
    print("3. Ajiaco")
    print("4. Sancocho")
    print("5. Arroz con coco")
    print("0. Salir")

    while True:
        try:
            num = int(input("Selecciona un plato: "))

            if num == 0:
                print("Gracias por visitar nuestro menu.")
                break

            dish = dish_fetch(num)

            if dish:
                print("Nombre:", dish["name"])
                print("Origen:", dish["origin"])
                print("Ingredientes:", ", ".join(dish["ingredients"]))
            else:
                print("Plato no encontrado.")

        except ValueError:
            print("Ingresa un numero valido.")


if __name__ == "__main__":
    main()
