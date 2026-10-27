from menu import Menu
import pickle
menu = Menu()
# try:
#     menu.add_item("پیتزا", 25000)
#     menu.add_item("برگر", 18000)
#     print("غذاها با موفقیت ثبت شدند")
#     print(menu.get_items())
#     print("منوی رستوران : ", menu.get_items())
#     price = menu.get_price("پیتزا")
#     print("قیمت پیتزا : ", price)
#     menu.remove_item("برگر")
#     print("منو بعد از حذف : ", menu.get_items())
# except ValueError as error:
#     print("خطا : ", error)
# try:
#     price = menu.get_price("ماکارونی")
#     print("قیمت ماکارونی : ", price)
# except ValueError as error:
#     print("خطای مورد انتظار : ", error)
#
# from customer import Customer
# try:
#     customer = Customer(
#     customer_id = 101,
#     first_name = "مجتبی",
#     last_name ="کفائی" ,
#     phone_number = "09123456789",
#     address = "میدان ولیعصر",
#     gender = "مرد")
# except ValueError as error:
#     print("خطای مورد انتظار : ", error)

# customer = Customer(
# customer_id = 101,
# first_name = "مجتبی",
# last_name ="کفائی" ,
# phone_number = "09123456789")
# print(customer.first_name)
# print(customer.address)
# print(customer.get_info())

# from order import Order

from menu import Menu
from customer import Customer
from order import Order

# ساخت منوی رستوران
restaurant_menu = Menu()
restaurant_menu.add_item("پیتزا", 250000)
restaurant_menu.add_item("برگر", 180000)

# ساخت مشتری
customer = Customer(
    customer_id=101,
    first_name="مجتبی",
    last_name="کفاشی",
    phone_number="09123456789"
)

# ساخت سفارش
order = Order(
    order_id=1001,
    customer=customer,
    menu=restaurant_menu
)

# بررسی ارتباط کلاس‌ها
print("شماره سفارش:", order.order_id)
print("نام مشتری:", order.customer.first_name)
print("منوی سفارش:", order.menu.get_items())

order.add_item("پیتزا", 2)
order.add_item("برگر", 1)
order.add_item("پیتزا", 1)

print("اقلام سفارش : ", order.get_items())
print("مبلغ کل :", order.calculate_total(), "تومان")
try:
    order.remove_item("برگر")

    print("سفارش بعد از حذف:", order.get_items())
    print("مبلغ جدید:", order.calculate_total(), "تومان")

except ValueError as error:
    print("خطا:", error)

# print("تاریخ و ساعت سفارش:", order.get_order_datetime())
# print(order.generate_invoice())
# order.save_order()
# print("سفارش با موفقیت ذخیره شد.")
# try:
#     # restored_order = Order.load_order()
#
#     print("سفارش بازیابی شد.")
#     print("شماره سفارش:", restored_order.order_id)
#     print("نام مشتری:", restored_order.customer.first_name)
#     print("اقلام سفارش:", restored_order.get_items())
#     print("مبلغ سفارش:", restored_order.calculate_total())
#
# except (OSError, ValueError, TypeError) as error:
#     print("خطا در بازیابی:", error)
# بازیابی سفارش اول
first_order = Order.load_order(1001)

# ساخت سفارش دوم
second_order = Order(
    order_id=1002,
    customer=customer,
    menu=restaurant_menu
)

second_order.add_item("برگر", 2)

# ذخیره سفارش دوم
# second_order.save_order()

# بازیابی هر دو سفارش
restored_first = Order.load_order(1001)
restored_second = Order.load_order(1002)

print("سفارش اول:", restored_first.get_items())
print("سفارش دوم:", restored_second.get_items())

print("مبلغ سفارش اول:", restored_first.calculate_total())
print("مبلغ سفارش دوم:", restored_second.calculate_total())
try:
    existing_order = Order.load_order(1001)
    existing_order.save_order()

except ValueError as error:
    print("تست جلوگیری از تکرار:", error)

from customer import Customer

try:
    test_customer = Customer(
        customer_id=2001,
        first_name="علی",
        last_name="رضایی",
        phone_number="09123456789",
        address="تهران، خیابان ولیعصر، پلاک ۱۲",
        gender="مرد"
    )

    test_customer.save_customer()

    print("مشتری با موفقیت ذخیره شد.")

    restored_customer = Customer.load_customer(2001)

    print("اطلاعات بازیابی‌شده:")
    print(restored_customer.get_info())

except (ValueError, OSError, EOFError, pickle.UnpicklingError) as error:
    print("خطا:", error)

from customer import Customer

try:
    customer = Customer.load_customer(2002)

    print("مشتری با موفقیت بازیابی شد.")
    print(customer.get_info())

except (ValueError, OSError) as error:
    print("خطا در بازیابی مشتری:", error)

from menu import Menu

try:
    test_menu = Menu()

    test_menu.add_item("پیتزا", 250000)
    test_menu.add_item("برگر", 180000)
    test_menu.add_item("پاستا", 220000)
    test_menu.add_item("سالاد سزار", 150000)
    test_menu.add_item("نوشابه", 30000)

    test_menu.save_menu()

    print("منو با موفقیت ذخیره شد.")

    restored_menu = Menu.load_menu()

    print("منوی بازیابی‌شده:")
    print(restored_menu.get_items())

except (ValueError, TypeError, OSError, EOFError,
        pickle.UnpicklingError) as error:
    print("خطا:", error)







