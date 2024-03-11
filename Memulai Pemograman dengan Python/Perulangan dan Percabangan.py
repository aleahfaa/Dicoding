"""
https://www.dicoding.com/academies/86/tutorials/6421?from=4769
TODO:
Buatlah sebuah variabel bertipe list bernama "evenNumber" dengan ketentuan:
- variabel tersebut menampung bilangan genap dari 0 hingga 500 (ingat 0 dan 500 termasuk).

Tips:
Anda bisa menggunakan loop dan if atau list comprehension untuk memudahkan.
"""

# TODO: Silakan buat kode Anda di bawah ini.
# madebyiffa(077)
evenNumber = [num for num in range (0, 501) if num % 2 == 0]
print(evenNumber)