from customer import Customer
from menu import Menu
from datetime import datetime
from persiantools.jdatetime import JalaliDateTime
import os
import pickle

class Order:
    def __init__(self, order_id: int, customer: Customer, menu: Menu) -> None:
        if type(order_id) is not int or order_id <= 0:
            raise ValueError("شماره سفارش باید عدد صحیخ مثبت باشد")
        if not isinstance(customer, Customer):
            raise TypeError("مشتری باید از کلاس Customer باشد")
        if not isinstance(menu, Menu):
            raise TypeError("منو باید از کلاس Menu باشد")

        self.order_id = order_id
        self.customer = customer
        self.menu = menu
        self._items = {}
        self.created_at = datetime.now()


    def add_item(self, name: str, quantity: int) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("نام غذا معتبر نیست.")

        if type(quantity) is not int or quantity <= 0:
            raise ValueError("تعداد غذا باید عدد صحیح مثبت باشد.")

        name = name.strip()
        price = self.menu.get_price(name)

        if name in self._items:
            self._items[name]["quantity"] += quantity
        else:
            self._items[name] = {
                "quantity": quantity,
                "price": price
            }

    def calculate_total(self) -> int:
        total = 0

        for item in self._items.values():
            total += item["price"] * item["quantity"]

        return total

    def remove_item(self, name: str) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("نام غذا معتبر نیست.")

        name = name.strip()

        if name not in self._items:
            raise ValueError("این غذا در سفارش وجود ندارد.")

        del self._items[name]

    def get_items(self) -> dict:
        return {
            name : details.copy() for name, details in
            self._items.items()
        }

    def get_order_datetime(self) -> str:
        jalali_date = JalaliDateTime(self.created_at)
        return jalali_date.strftime("%Y/%m/%d - %H:%M:%S")

    def generate_invoice(self) -> str:
        lines = [
            "========== فاکتور رستوران ==========",
            f"شماره سفارش: {self.order_id}",
            f"نام مشتری: {self.customer.first_name} {self.customer.last_name}",
            f"شماره تماس: {self.customer.phone_number}",
            f"تاریخ سفارش: {self.get_order_datetime()}",
            "------------------------------------"
        ]

        for name, details in self._items.items():
            quantity = details["quantity"]
            price = details["price"]
            subtotal = quantity * price

            lines.append(
                f"{name} | تعداد: {quantity} | "
                f"قیمت واحد: {price:,} | "
                f"جمع: {subtotal:,} تومان"
            )

        lines.append("------------------------------------")
        lines.append(
            f"مبلغ کل: {self.calculate_total():,} تومان"
        )
        lines.append("====================================")

        return "\n".join(lines)

    def save_order(self, filename: str = "data/orders.pkl") -> None:
        folder = os.path.dirname(filename)

        try:
            if folder:
                os.makedirs(folder, exist_ok=True)

            orders = {}

            if os.path.isfile(filename):
                with open(filename, "rb") as file:
                    orders = pickle.load(file)

                if not isinstance(orders, dict):
                    raise ValueError("ساختار فایل سفارش‌ها معتبر نیست.")
            if self.order_id in orders:
                raise ValueError(
                    f"سفارش شماره {self.order_id} قبلاً ثبت شده است."
                )

            orders[self.order_id] = self

            with open(filename, "wb") as file:
                pickle.dump(orders, file)

        except (OSError, pickle.UnpicklingError, EOFError) as error:
            raise ValueError(f"خطا در ذخیره سفارش: {error}") from error

    @staticmethod
    def load_order(
        order_id: int,
        filename: str = "data/orders.pkl"
    ) -> "Order":

        if not os.path.isfile(filename):
            raise FileNotFoundError("فایل سفارش‌ها وجود ندارد.")

        try:
            with open(filename, "rb") as file:
                orders = pickle.load(file)

        except (OSError, pickle.UnpicklingError, EOFError) as error:
            raise ValueError(f"خطا در بازیابی: {error}") from error

        if not isinstance(orders, dict):
            raise ValueError("ساختار فایل سفارش‌ها معتبر نیست.")

        if order_id not in orders:
            raise ValueError("شماره سفارش پیدا نشد.")

        order = orders[order_id]

        if not isinstance(order, Order):
            raise TypeError("اطلاعات سفارش معتبر نیست.")

        return order

    @staticmethod
    def get_next_order_id(
        filename: str = "data/orders.pkl"
    ) -> int:

        if not os.path.isfile(filename):
            return 1001

        try:
            with open(filename, "rb") as file:
                orders = pickle.load(file)

            if not isinstance(orders, dict):
                raise ValueError("ساختار فایل سفارش‌ها معتبر نیست.")

            if not orders:
                return 1001

            if any(type(key) is not int for key in orders):
                raise ValueError("شناسه سفارش‌ها معتبر نیست.")

            return max(1000, max(orders.keys())) + 1

        except (OSError, pickle.UnpicklingError, EOFError) as error:
            raise ValueError(
                f"خطا در خواندن شماره سفارش: {error}"
            ) from error

