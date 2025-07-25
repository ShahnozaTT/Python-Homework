# # Homework

# ## Task
# Learn about `map` and `filter` functions, and be prepared to explain them in class. Provide examples using these functions with `lambda` expressions.

# ---

# # Problems

# ## 1. is_prime(n) funksiyasi
# `is_prime(n)` funksiyasini hosil qiling (`n > 0`). Agar `n` soni tub bo'lsa `True`, aks holda `False` qiymat qaytarsin.

# ### Misollar:
# - **Kiritish:**  
#   4  
#   **Natija:**  
#   False  
#   _(Izoh: 4 soni tub emas, chunki u 2 ga bo'linadi.)_

# - **Kiritish:**  
#   7  
#   **Natija:**  
#   True  
#   _(Izoh: 7 soni faqat 1 va o'ziga bo'linadi, ya'ni tub son.)_

# n = int(input("Son kiriting: "))
# def is_prime(n):
#     if n <= 1:
#         return False  # 0 va 1 tub emas
#     if n == 2:
#         return True   # 2 tub son
    
#     for i in range(2, n):
#         if n % i == 0:
#             return False  # Bo'linadi, demak tub emas
#     return True  # Hech qaysi songa bo'linmaydi, demak tub

# print(is_prime(n))


# ## 2. digit_sum(k) funksiyasi
# `digit_sum(k)` funksiyasini yozing, u `k` sonining raqamlari yig'indisini hisoblaydi.

# ### Misollar:
# - **Kiritish:**  
#   24  
#   **Natija:**  
#   6  
#   _(Izoh: 24 sonining raqamlari yig'indisi: 2 + 4 = 6.)_

# - **Kiritish:**  
#   502  
#   **Natija:**  
#   7  
#   _(Izoh: 502 sonining raqamlari yig'indisi: 5 + 0 + 2 = 7.)_

# def digit_sum(k):
#     return sum(int(digit) for digit in str(k))

# k = int(input("Son kiriting: "))
# print("Raqamlar yig'indisi:", digit_sum(k))



# ## 3. Ikki sonning darajalari
# Berilgan `N` sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, `2**k` shaklidagi sonlarni) chop etuvchi funksiyani yozing.

# ### Misol:
# - **Kiritish:**  
#   10  
#   **Natija:**  
#   2 4 8  
#   _(Izoh: 10 dan kichik yoki teng bo'lgan 2 ning darajalari: 2, 4, 8.)_


# N = int(input("N sonini kiriting: "))

# current = 2
# while current <= N:
#     print(current, end=' ')
#     current *= 2  # current = current * 2





