import time

# Mulai pengukuran waktu
start_time = time.time()

import itertools
from itertools import combinations

# Define the Mobil class
class Mobil:
    def __init__(self, nama, kapasitas, km_per_liter, biaya_sewa):
        self.nama = nama
        self.kapasitas = kapasitas
        self.km_per_liter = km_per_liter
        self.biaya_sewa = biaya_sewa

    def __repr__(self):
        return f"Mobil({self.nama}, Kapasitas: {self.kapasitas}, Km/liter: {self.km_per_liter}, Biaya sewa: {self.biaya_sewa})"

# List of cars
cars = [
    Mobil('Honda CRV', 7, 12.6, 650000),
    Mobil('Toyota Innova', 7, 9.7, 600000),
    Mobil('Toyota Innova Zenix', 7, 15, 750000),
    Mobil('Hyundai Stargazer', 7, 14, 550000),
    Mobil('Honda Civic CDF', 4, 14, 380000),
    Mobil('Daihatsu Ayla', 5, 25, 300000),
    Mobil('Toyota Hiace', 13, 9, 1500000)
]

#---------------------------------------------------------------------------------------------------------------------------------

import itertools
from itertools import combinations

# Data perjalanan
edges = [
    (1, 2, False, 20, 0),
    (2, 3, True, 10, 7000),
    (2, 4, False, 3, 0),
    (3, 8, True, 5, 12000),
    (4, 6, False, 10, 0),
    (6, 7, False, 10, 0),
    (7, 8, False, 18, 0),
    (1, 5, True, 7, 5000),
    (5, 6, False, 7, 0)
]

# Representasi graf
graph = {}
for frm, to, jenis, weight, price in edges:
    if frm not in graph:
        graph[frm] = []
    graph[frm].append((to, weight, price))

# Fungsi untuk menemukan semua jalur dari start ke end
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for (node, weight, price) in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for p in newpaths:
                paths.append(p)
    return paths

# Fungsi untuk menghitung total berat dan biaya dari sebuah jalur
def calculate_weight_and_price(path, graph):
    total_weight = 0
    total_price = 0
    for i in range(len(path) - 1):
        for (node, weight, price) in graph[path[i]]:
            if node == path[i + 1]:
                total_weight += weight
                total_price += price
                break
    return total_weight, total_price

# Menemukan semua jalur dari 1 ke 8
all_paths = find_all_paths(graph, 1, 8)

# Menghitung total berat dan biaya untuk setiap jalur
path_weights_prices = []
for path in all_paths:
    weight, price = calculate_weight_and_price(path, graph)
    path_weights_prices.append((path, weight, price))

# Menampilkan semua jalur beserta total berat dan biaya
for path, weight, price in path_weights_prices:
    print(f"Path: {path}, Total Weight: {weight}, Total Price: {price}")

# Menemukan jalur dengan berat minimum
min_weight_path = min(path_weights_prices, key=lambda x: x[1])
print(f"Minimum Weight Path: {min_weight_path[0]}, Total Weight: {min_weight_path[1]}, Total Price: {min_weight_path[2]}")

# Menemukan jalur dengan harga minimum
min_price_path = min(path_weights_prices, key=lambda x: x[2])
print(f"Minimum Price Path: {min_price_path[0]}, Total Weight: {min_price_path[1]}, Total Price: {min_price_path[2]}")

print()
#--------------------------------------------------------------------------------------------------------------------------------


# Total people to transport
total_people = 12
# Distance of the trip
distance = min_weight_path[1]
# Cost of one liter of fuel
fuel_cost_per_liter = 12000

tol = min_weight_path[2]

# Function to calculate total cost for a combination of cars
def calculate_cost(car_combination, distance, fuel_cost_per_liter):
    total_rental_cost = sum(car.biaya_sewa for car in car_combination)
    total_fuel_cost = sum((distance / car.km_per_liter) * fuel_cost_per_liter for car in car_combination)
    total_cost = int(total_rental_cost + total_fuel_cost)  # Convert to integer
    return total_cost

# Function to check if a combination of cars can transport the required number of people
def can_transport_people(car_combination, total_people):
    return sum(car.kapasitas for car in car_combination) >= total_people

# Find the best combination of cars
best_combination = None
min_cost = float('inf')
unused_combinations = []

# Generate all possible combinations of cars
for r in range(1, len(cars) + 1):
    for combination in combinations(cars, r):
        if can_transport_people(combination, total_people):
            cost = calculate_cost(combination, distance, fuel_cost_per_liter)
            if cost < min_cost:
                min_cost = cost
                best_combination = combination
        else:
            unused_combinations.append(combination)

# Print the best combination of cars
if best_combination:
    print("Kombinasi mobil terbaik untuk disewa (weight path):")
    for car in best_combination:
        print(f"{car.nama} - Kapasitas: {car.kapasitas}, Km/liter: {car.km_per_liter}, Biaya sewa: {car.biaya_sewa}")
    print(f"Total biaya: {min_cost + tol}")
else:
    print("Tidak ada kombinasi mobil yang dapat mengangkut jumlah orang yang dibutuhkan.")

print()
# Print the unused combinations
print("\nKombinasi mobil yang tidak terpakai:")
for combination in unused_combinations:
    print([car.nama for car in combination])
print()
#--------------------------------------------------------------------------------------------------------------------------------------

# Distance of the trip
distance = min_price_path[1]
tol = min_price_path[2]

# Find the best combination of cars
best_combination = None
min_cost = float('inf')
unused_combinations = []

# Generate all possible combinations of cars
for r in range(1, len(cars) + 1):
    for combination in combinations(cars, r):
        if can_transport_people(combination, total_people):
            cost = calculate_cost(combination, distance, fuel_cost_per_liter)
            if cost < min_cost:
                min_cost = cost
                best_combination = combination
        else:
            unused_combinations.append(combination)


# Print the best combination of cars
if best_combination:
    print("Kombinasi mobil terbaik untuk disewa (price path):")
    for car in best_combination:
        print(f"{car.nama} - Kapasitas: {car.kapasitas}, Km/liter: {car.km_per_liter}, Biaya sewa: {car.biaya_sewa}")
    print(f"Total biaya: {min_cost + tol}")
else:
    print("Tidak ada kombinasi mobil yang dapat mengangkut jumlah orang yang dibutuhkan.")


# Print the unused combinations
print("\nKombinasi mobil yang tidak terpakai:")
for combination in unused_combinations:
    print([car.nama for car in combination])


# Selesai pengukuran waktu
end_time = time.time()

# Hitung total waktu eksekusi
execution_time = end_time - start_time
print()
print(f"Total execution time: {execution_time} seconds")
