import os
import pickle

class Customer:
    def __init__(self, customer_id: int, first_name: str, last_name: str, phone_number: str,address: str = "", gender: str = "") -> None:
        if type(customer_id) is not int or customer_id<= 0:
            raise ValueError("شناسه مشتری باید عدد صحیح مثبت باشد")
        if not isinstance(first_name, str) or not first_name.strip():
            raise ValueError("نام معتبر نیست")
        if not isinstance(last_name, str) or not last_name.strip():
            raise ValueError("نام خانوادگی معتبر نیست")
        if not isinstance(phone_number, str) or not phone_number.strip() or len(phone_number) != 11 or not phone_number.startswith("09") or not phone_number.isascii() or not phone_number.isdigit():
            raise ValueError("شماره موبایل با 09 شروع شود و 11 رقم باشد")
        if not isinstance(address, str):
            raise ValueError("آدرس صحیح نمی باشد")
        if not isinstance(gender, str):
            raise ValueError("جنسیت صحیح نمی باشد")
        if gender.strip() not in ("", "مرد", "زن", "سایر"):
            raise ValueError("جنسیت معتبر نیست")

        self.customer_id = customer_id
        self.first_name = first_name.strip()
        self.phone_number = phone_number
        self.last_name = last_name.strip()
        self.address = address.strip()
        self.gender = gender.strip()

    def get_info(self) -> dict:
        return {
            self.customer_id : "شناسه",
            self.first_name : "نام",
            self.last_name : "نام خانوادگی",
            self.phone_number : "شماره تماس",
            self.address : "آدرس",
            self.gender : "جنسیت"
        }

    def save_customer(self, filename="data/customers.pkl"):

        os.makedirs(
            os.path.dirname(filename),
            exist_ok=True
        )

        customers = {}

        if os.path.exists(filename):
            with open(filename, "rb") as file:
                customers = pickle.load(file)

        if not isinstance(customers, dict):
            raise ValueError(
                "ساختار فایل مشتریان معتبر نیست."
            )

        if self.customer_id in customers:
            raise ValueError(
                f"مشتری با شناسه {self.customer_id} قبلاً ثبت شده است."
            )

        customers[self.customer_id] = self

        with open(filename, "wb") as file:
            pickle.dump(customers, file)

    @staticmethod
    def load_customer(
        customer_id: int,
        filename="data/customers.pkl"
    ):

        if not os.path.isfile(filename):
            raise FileNotFoundError(
                "فایل اطلاعات مشتریان وجود ندارد."
            )

        with open(filename, "rb") as file:
            customers = pickle.load(file)

        if not isinstance(customers, dict):
            raise ValueError(
                "ساختار فایل مشتریان معتبر نیست."
            )

        if customer_id not in customers:
            raise ValueError(
                f"مشتری با شناسه {customer_id} پیدا نشد."
            )

        return customers[customer_id]
    @staticmethod
    def load_all_customers(filename="data/customers.pkl"):
        if not os.path.isfile(filename):
            return {}

        with open(filename, "rb") as file:
            customers = pickle.load(file)

        if not isinstance(customers, dict):
            raise ValueError("ساختار فایل مشتریان معتبر نیست.")

        return customers

    def update_customer(self, filename="data/customers.pkl"):

        if not os.path.isfile(filename):
            raise FileNotFoundError(
                "فایل اطلاعات مشتریان وجود ندارد."
            )

        with open(filename, "rb") as file:
            customers = pickle.load(file)

        if not isinstance(customers, dict):
            raise ValueError("ساختار فایل مشتریان معتبر نیست.")

        if self.customer_id not in customers:
            raise ValueError("مشتری موردنظر پیدا نشد.")

        customers[self.customer_id] = self

        with open(filename, "wb") as file:
            pickle.dump(customers, file)

    @staticmethod
    def delete_customer(
        customer_id: int,
        filename="data/customers.pkl"
    ):
        if not os.path.isfile(filename):
            raise FileNotFoundError(
                "فایل اطلاعات مشتریان وجود ندارد."
            )

        with open(filename, "rb") as file:
            customers = pickle.load(file)

        if not isinstance(customers, dict):
            raise ValueError(
                "ساختار فایل مشتریان معتبر نیست."
            )

        if customer_id not in customers:
            raise ValueError(
                "مشتری موردنظر پیدا نشد."
            )

        del customers[customer_id]

        with open(filename, "wb") as file:
            pickle.dump(customers, file)

