import os
import pickle
from order import Order

filename = "data/orders.pkl"

if not os.path.isfile(filename):
    print("فایل سفارش‌ها وجود ندارد.")
else:
    try:
        with open(filename, "rb") as file:
            data = pickle.load(file)

        if isinstance(data, Order):
            with open(filename, "wb") as file:
                pickle.dump({data.order_id: data}, file)

            print("فایل قدیمی با موفقیت تبدیل شد.")

        elif isinstance(data, dict):
            print("فایل از قبل ساختار جدید دارد.")

        else:
            print("ساختار فایل شناخته‌شده نیست.")

    except (OSError, pickle.UnpicklingError, EOFError) as error:
        print("خطا در تبدیل فایل:", error)