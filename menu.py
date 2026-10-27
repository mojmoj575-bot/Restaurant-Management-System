import os
import pickle

class Menu:
    def __init__(self):
        self._items = {}

    def add_item(self, name: str, price: int) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("نام غذا معتبر نیست")
        if not isinstance(price, int) or isinstance(price, bool) or price <= 0:
            raise ValueError("قیمت باید یک عدد صحیح مثبت باشد")
        name = name.strip()
        if name in self._items:
            raise ValueError("این غذا قبلأ در منو ثبت شده است")
        self._items[name] = price

    def remove_item(self, name: str) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("نام غذا معتبر نیست")
        name = name.strip()
        if name not in self._items:
            raise ValueError("این غذا در منو وجود ندارد")
        del self._items[name]
    def get_items(self) -> dict:
        return self._items.copy()

    def get_price(self, name: str) -> int:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("نام غذا معتبر نیست")
        name = name.strip()
        if name not in self._items:
            raise ValueError("این غذا در منو وجود ندارد")
        return self._items[name]

    def save_menu(self, filename="data/menu.pkl"):

        folder = os.path.dirname(filename)

        if folder:
            os.makedirs(folder, exist_ok=True)

        temp_filename = filename + ".tmp"

        try:
            with open(temp_filename, "wb") as file:
                pickle.dump(self._items, file)

            os.replace(temp_filename, filename)

        finally:
            if os.path.exists(temp_filename):
                os.remove(temp_filename)

    @staticmethod
    def load_menu(filename="data/menu.pkl"):

        if not os.path.isfile(filename):
            raise FileNotFoundError(
                "فایل منوی رستوران وجود ندارد."
            )

        with open(filename, "rb") as file:
            items = pickle.load(file)

        if not isinstance(items, dict):
            raise ValueError(
                "ساختار فایل منو معتبر نیست."
            )

        menu = Menu()

        for name, price in items.items():
            menu.add_item(name, price)

        return menu

    def update_price(self, name: str, new_price: int):
        if not isinstance(name, str) or name not in self._items:
            raise ValueError("غذای موردنظر در منو وجود ندارد.")

        if type(new_price) is not int or new_price <= 0:
            raise ValueError("قیمت جدید باید یک عدد صحیح مثبت باشد.")

        self._items[name] = new_price

    def remove_item(self, name: str):
        if not isinstance(name, str) or name not in self._items:
            raise ValueError("غذای موردنظر در منو وجود ندارد.")

        del self._items[name]













