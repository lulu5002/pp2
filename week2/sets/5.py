set1 = {"s", "o", "k"}
set2 = {123, 456, 789}
set3 = set1.union(set2)
print(set3)

set1 = {"s", "o", "k"}
set2 = {123, 456, 789}
set1.update(set2)
print(set1)

x = {"facebook", "yandex", "google"}
y = {"google", "meta", "microsoft"}
x.intersection_update(y)
print(x)

x = {"facebook", "yandex", "google"}
y = {"google", "meta", "microsoft"}
z = x.intersection(y)
print(z)

x = {"facebook", "yandex", "google"}
y = {"google", "meta", "microsoft"}
x.symmetric_difference_update(y)
print(x)

x = {"facebook", "yandex", "google"}
y = {"google", "meta", "microsoft"}
z = x.symmetric_difference(y)
print(z)