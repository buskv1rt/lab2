from dataclasses import dataclass
from enum import Enum


class StockOperation(Enum):
    RECEIPT = "Надходження"
    WRITE_OFF = "Списання"


@dataclass
class InventoryItem:
    name: str
    quantity: int
    price: float
    status: str = "Доступний"

    def __post_init__(self):
        if not self.name.strip():
            raise ValueError("Назва товару не може бути порожньою")

        if self.quantity < 0:
            raise ValueError("Кількість товару не може бути від'ємною")

        if self.price < 0:
            raise ValueError("Ціна товару не може бути від'ємною")

        if not self.status.strip():
            raise ValueError("Стан товару не може бути порожнім")


class Warehouse:
    def __init__(self, name, address):
        self._items = []
        self.name = name
        self.address = address

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Назва складу не може бути порожньою")

        self._name = value.strip()

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if not value.strip():
            raise ValueError("Адреса складу не може бути порожньою")

        self._address = value.strip()

    def add_item(self, item):
        if not isinstance(item, InventoryItem):
            raise ValueError("На склад можна додати тільки товар")

        self._items.append(item)

    def show_items(self):
        if not self._items:
            print("\nНа складі немає товарів.")
            return

        print("\nТовари на складі:")

        for item in self._items:
            print(
                f"Назва: {item.name}, "
                f"Кількість: {item.quantity}, "
                f"Ціна: {item.price:.2f} грн, "
                f"Стан: {item.status}"
            )


def input_required_text(message, error_message):
    while True:
        value = input(message)

        if not value.strip():
            print(f"Помилка: {error_message}")
            continue

        return value.strip()


def input_quantity():
    while True:
        value = input("Введіть кількість товару: ")

        try:
            quantity = int(value)
        except ValueError:
            print("Помилка: кількість товару повинна бути цілим числом.")
            continue

        if quantity < 0:
            print("Помилка: кількість товару не може бути від'ємною.")
            continue

        return quantity


def input_price():
    while True:
        value = input("Введіть ціну товару: ")

        try:
            price = float(value)
        except ValueError:
            print("Помилка: ціна товару повинна бути числом.")
            continue

        if price < 0:
            print("Помилка: ціна товару не може бути від'ємною.")
            continue

        return price


if __name__ == "__main__":
    print("=== Система обліку складських запасів ===")

    while True:
        try:
            warehouse_name = input_required_text(
                "Введіть назву складу: ",
                "назва складу не може бути порожньою."
            )

            warehouse_address = input_required_text(
                "Введіть адресу складу: ",
                "адреса складу не може бути порожньою."
            )

            warehouse = Warehouse(
                warehouse_name,
                warehouse_address
            )

            break

        except ValueError as error:
            print(f"Помилка: {error}")

    print("\n--- Дані товару ---")

    item_name = input_required_text(
        "Введіть назву товару: ",
        "назва товару не може бути порожньою."
    )

    item_quantity = input_quantity()

    item_price = input_price()

    item_status = input_required_text(
        "Введіть стан товару: ",
        "стан товару не може бути порожнім."
    )

    while True:
        try:
            item = InventoryItem(
                item_name,
                item_quantity,
                item_price,
                item_status
            )

            warehouse.add_item(item)
            break

        except ValueError as error:
            print(f"Помилка: {error}")

    print("\nТовар успішно додано!")
    warehouse.show_items()

    operation = StockOperation.RECEIPT

    print(f"\nТип операції: {operation.value}")

    print("\nВнутрішній стан товару:")
    print(vars(item))

    print("\nВнутрішній стан складу:")
    print(vars(warehouse))