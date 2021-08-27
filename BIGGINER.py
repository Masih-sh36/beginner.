# برای نمایش طول و تعداد  len
# برای نمایش و ادرس دادن استرینگ ها variable[number]
# variable = متغیر
# value = ارزش

import math
x = "hello world"
print(len(x))
print(x[0])
print(x[0:3])
print(x[:])
print(x[0:])
print(x[:3])

print("\n\n/////////////")

# برای فرار داریم
# \'
# \"
# \\
# \n
# برای بزرگ نمایی print(variable.upper())
# برای کوچیک کردن print(variable.lower())
# برای کپیتال کردن حروف اول print(variable.title())
# برای از بین بردن فضاهای خالی print(variable.strip())
# برای ادر س مستقیم عضو print(variable.find("memmbers"))
# برای جایگذاری عضو هی print(variable.replace("..","..."))
# برای چک کردن عضوی در متغیر print("..." in variable) = boolean(true,false)
#                             print("..." not in variable)
y = "hi \"beach"
print(y)
y = "hi \nbeach"
print(y)

case = "  mohammad  "
print(case.upper())
print(case.lower())
print(case.title())
print(case.strip())
print(case.find("mo"))
print(case.replace("m", "c"))
print("mo" in case)
print("mo" not in case)

print(" \n\n/////////////")
# این دستور برای حا کردن تابع در استرینگ میباشد
# برای نمایش دادن ترکیبات
# + +
# f"{} {}"
# وقتی از {} استفاده میکنیم هرچیزیو میتونی درونش قرار بدیم
x = 4
print(f"we have {x} apples")

name = "masih"
last_name = "shatery"
full_name = name + " " + last_name
print(full_name)
# or f"{name} {last_name}
full_name = f"{name} {last_name}"
print(full_name)

print("\n\n////////////")

# عملگرها

print(1+2)
print(2-1)
print(2*2)
print(2**3)  # توان **
print(10/3)
print(10//3)  # جذز //
print(10 % 3)  # درصد %
x = 3
x = x + 10
# یا
x += 3
print(x)
# گرد کردن print(round())
# برای نمایش ارزش واقعی عدد print(abs())
# برای نمایش سقف عدد نیاز به ورودی داریم import variable
print(round(4.9))
print(abs(-3.10))
print(math.ceil(2.9))

print("\n\n////////////////")

# حالت ورودی variable = input('...')
# برای نشان دادن نوع کد print(type(variable))
x = input('x= ')
y = int(x) + 1
print(f'x:{x} , y:{y}')
# برای جواب گیری حتما از ترمینال استفاده شود
# اگر اینها در بولین بکار رود در هر صورت جواب فالسه
bool("")
bool(0)
bool()

print("\n/////////")
# عملگرهای مقایسه ای booleans(True,False)
x = 10 > 1
print(x)
y = 2 >= 1
print(y)
z = 3 < 1
print(z)
n = 3 <= 1
print(n)
s = 12 == 12
print(s)
r = 12 == "12"
print(r)
c = 13 != 14
print(c)
g = 13 != "14"
print(g)
# حال برای مقایسه کلمات
x = "bill" > "apple"
print(x)
y = "bill" > "BILL"
print(y)
z = "BILL" > "bill"
print(z)
# هیچ تفاوتی ندارن فقط فونت کلمات مقایسه ایجاد می کنند به دلیل زیر
print(ord("B"))
print(ord("b"))
# هیچ نیازی به یادگرفتن دستور اورد نیست فقط برای مقایسه و جای لغات در الفابت پایتون استفاده میشه

print('\n///////')

# ازین دستور برای تصمیم گیری استفاده میشود که به به بولین ها مربوط است if variable .... :
tempreture = 35
if tempreture > 20:
    print("the weather is warm")
    print("drink water")
print("Done")
# حالا اگه رابطه درست نبود یعنی ترو نباشه دستور های زیر ایف اجار نشده و اخرین دستور بیرون از زنجیر ایف اجرا میشه
tempreture = 19
if tempreture > 20:
    print("the weather is warm")
    print("drink water")
print("Done")
# برای اینکه دستور دیگه درصورت درست نبودن دستور قبلی ایجاد بشه استفاده میشه elif varieble:
tempreture = 19
if tempreture > 20:
    print("the weather is warm")
    print("drink water")
elif tempreture > 12:
    print("ok thats good")
print("Done")
# حالا اگه هیچ کدوم درست نبود از این دستور استفاده میکنیم else:
tempreture = 19
if tempreture > 20:
    print("the weather is warm")
    print("drink water")
elif tempreture > 21:
    print("ok thats good")
else:
    print("ok the its cold")
print("Done")

# حال با استفاده از یک ارزش در تابع شروع میکنیم
tempreture = 30
if tempreture > 20:
    massage = "warm"
else:
    massage = "cold"
print(massage)
# راه دیگه value = "..." if .... else "...."
tempreture = 30
massage = "warm" if tempreture > 20 else "cold"
print(massage)

print("\n///////")
# and
# or
# not
# در این قسمت هردو بولین (باید) باهم برابر باشند and
income = True
credit = True

if income and credit:
    print("its logical")
# برای منفی کردن قضیه
income = False
credit = True

if income and credit:
    print("its logical")
else:
    print("its not logical")
# در این قسمت یکی درست باشه قضیه اوکیه or
income = False
credit = True

if income or credit:
    print("its logical")
else:
    print("its not logical")
# در اینجا باید پشته بولین قرار بگیره که منفی میکنه تابع روnot vsriable
income = False
credit = True
logic = True
if not logic:
    print("its logical")
else:
    print("its not logical")
# برای ترکیب همه باهم
income = False
credit = True
logic = True
if (income or credit) and not logic:
    print("its logical")
else:
    print("its not logical")
# نوشتن حالت مختلف دستور ایف به زبان ریاضی
# age should be between 18 and 65
age = 22
if age >= 18 and age < 65:
    # نمایش حالت ریاضی
if 18 <= age < 65:
    print("its right")

print("\n///////")

# معرفی (loop)
# اگر بخواهیم پیغامی چندین بار تکرار شود ازش استفاده میکنیم for number in range(..):
for number in range(5):
    print("hi")
# در اینجا یک اینتیجر است number
# برای ادرس دادن در این دستور داریم
for number in range(5):
    print("hi", number)
# میشه عدد هم اضافه کرد
for number in range(5):
    print("hi", number + 1)
# برای اضافه کردن یک چیزی جلوی خروجی هم داریم
for number in range(5):
    print("hi", number + 1, (number + 1) * "...")
# راه دیگه ای هم برای اجرای کد 235 داریم
for number in range(5, 9):
    print("hi", number, number * "...")
# یا
for number in range(5, 20, 6):
    print("hi", number, number * "...")
# یعنی عدد اخر بعلاوه عدد اول تا نهایت بغیر از عدد وسط(x,z,y)

print("\n///////")
# ترکیب کردن لوپ و ایف
seccessful = True
for number in range(3):
    print("attempt")
    if seccessful:
        print("all done")
        break
# برای خلاصه کردن و نشون دادن جواب نهایی استفاده میشه و فقط برای لوپ هاست break
# حال اگه تابع درست نباشه
seccessful = False
for number in range(3):
    print("attempt")
    if seccessful:
        print("all done")
        break
else:
    print("that was a mistake")

print("\n///////")

# ترکیب کردن لوپ ها
for x in range(5):
    for y in range(3):
        print(f"({x},{y})")
# در لوپ ها میتونیم از استرینگ ها و لیست های اعداد هم استفاده کنیم
for x in "python":
    print(x)
for y in [1, 2, 3, 4, 5, 6, 7]:  # lists
    print(y)

print("\n///////")
# یکی دیگر از لوپ ها while
number = 20
while number > 1:
    print(number)
    number /= 2
# مثل لوپ قبلی هر نوع دستوری رو میشه توی این لوپ هم بزاریم
command = ""
while command != "exit":
    command = input(">")
    print("REAPEAT", command)
# گفتیم این دستور حتما تو ترمینال در وی اس کد اجرا بشه input

print("\n//////")
# برای تعریف کردن یا به عبارتی ساختن یک عملگر به نام خودتون ازاین دستور استفاده می کنیم def ....()
#                                                                                        print(..)


def hi():
    print("hello world")
    print("whats up")


hi()
# حالا میتونیم به عملگرمون یک معنی داده و ئر عبارت اخر ارزش های اون معنی رو بنویسیم


def hi(first_name, last_name):
    print(f"hello {first_name} , {last_name}")
    print("whats up")


hi("mohammad", "ali")  # معنی های عملگرمونو تعریف میکنیم

# حال بجای پرینت از این عبارت استفاده میکنیم چون کیفیت و مشکلی در اینده برای این عملگر اجرا نمی کنه return
# و می تونیم چندین تابع زیرش بسازیم
# یچور برگشت به معنیه ارزش میمونه
# مثل این دستور f"{}{}"


def increment(number, by):
    return number + by


result = increment(2, 1)
print(result)
# روش دیگه برای نشون دادن نتیجه


def increment(number, by):
    return number + by


print(increment(2, 1))
# یا


def increment(number, by=1):
    return number + by


print(increment(2))

# یا


def increment(number, by=1):
    return number + by


print(increment(2, 5))
# برای مساوی قرار دادن ارزش های عملگر حتما تو قسمت اخر باید باشن


def increment(number, by=1, another):  # غلط شد
    return number + by


print(increment(2, 5))


def increment(number, another, by=1):  # درسته
    return number + by


print(increment(2, 5))

# لیستی از اعداد هم میتونیم درست کنیم
[1, 2, 3, 4, 5]


def num(*numbers):
    print(numbers)


num(1, 2, 3, 4, 5)
# حال با استفاده از لوپ ها داریم


def num(*numbers):
    for number in numbers:
        print(number)


num(1, 2, 3, 4, 5)

print("\n\n/////////////")

# نکته ای کلیدی در ساختن دیکشنریست **


def user_name(**user):
    print(user)


user_name(id=12, name="ali", age=23)  # خروجی که مشاهده میکنید دیکشنری نام دارد
# ''بین نام هاست **       # **=''

# برای دسترسی به عضو های دیکشنری به این صورت عمل میکنیم


def user_name(**user):
    print(user["id"])  # یا هر تابع دیگری در غالب استرینگ


user_name(id=12, name="ali", age=23)
