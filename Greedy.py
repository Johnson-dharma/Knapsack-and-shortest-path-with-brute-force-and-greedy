import time

# Mulai pengukuran waktu
start_time = time.time()

class Mobil:
    def __init__(self, nama, kapasitas, km_per_liter, biaya_sewa):
        self.nama = nama
        self.kapasitas = kapasitas
        self.km_per_liter = km_per_liter
        self.biaya_sewa = biaya_sewa

    def biaya_bahan_bakar(self, jarak, harga_per_liter):
        return int((jarak / self.km_per_liter) * harga_per_liter)

def greedy_mobil_by_kapasitas(mobil_list, orang):
    mobil_list.sort(key=lambda x: x.kapasitas, reverse=True)
    selected_mobil = []
    total_orang = 0

    for mobil in mobil_list:
        if total_orang >= orang:
            break
        selected_mobil.append(mobil)
        total_orang += mobil.kapasitas

    return selected_mobil

def greedy_mobil_by_efisiensi_bahan_bakar(mobil_list, jarak, harga_per_liter):
    mobil_list.sort(key=lambda x: x.biaya_bahan_bakar(jarak, harga_per_liter))
    selected_mobil = []
    total_orang = 0

    for mobil in mobil_list:
        if total_orang >= orang:
            break
        selected_mobil.append(mobil)
        total_orang += mobil.kapasitas

    return selected_mobil

def greedy_mobil_by_biaya_sewa(mobil_list, orang):
    mobil_list.sort(key=lambda x: x.biaya_sewa)
    selected_mobil = []
    total_orang = 0

    for mobil in mobil_list:
        if total_orang >= orang:
            break
        selected_mobil.append(mobil)
        total_orang += mobil.kapasitas

    return selected_mobil

def greedy_mobil_by_density(mobil_list, orang, BBM):
    mobil_list.sort(key=lambda x: (x.biaya_sewa + BBM)/ x.kapasitas)
    selected_mobil = []
    total_orang = 0

    for mobil in mobil_list:
        if total_orang >= orang:
            break
        selected_mobil.append(mobil)
        total_orang += mobil.kapasitas

    return selected_mobil

def total_biaya(selected_mobil, jarak, harga_per_liter):
    total_sewa = sum(mobil.biaya_sewa for mobil in selected_mobil)
    total_bahan_bakar = sum(mobil.biaya_bahan_bakar(jarak, harga_per_liter) for mobil in selected_mobil)
    return int(total_sewa + total_bahan_bakar)

# Contoh data
mobil_list = [
    Mobil('Honda CRV', 7, 12.6, 650000),
    Mobil('Toyota Innova', 7, 9.7, 600000),
    Mobil('Toyota Innova Zenix', 7, 15, 750000),
    Mobil('Hyundai Stargazer', 7, 14, 550000),
    Mobil('Honda Civic CDF', 4, 14, 380000),
    Mobil('Daihatsu Ayla', 5, 25, 300000),
    Mobil('Toyota Hiace', 13, 9, 1500000)
]

#-----------------------------------------------------------------------------------------------------------------------------------
class Edge:
    def __init__(self, from_node, to_node, weight, is_toll, price):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight
        self.is_toll = is_toll
        self.price = price

# Data edges: (from, to, weight, jenis (jalan tol = True, jalan biasa = False), price)
edges = [
    Edge(1, 2, 20, False, 0),
    Edge(2, 3, 10, True, 7000),
    Edge(2, 4, 3, False, 0),
    Edge(3, 8, 5, True, 12000),
    Edge(4, 6, 10, False, 0),
    Edge(6, 7, 10, False, 0),
    Edge(7, 8, 18, False, 0),
    Edge(1, 5, 7, True, 5000),
    Edge(5, 6, 7, False, 0)
]

def find_next_node_weight(current_node, visited, edges):
    min_weight = float('inf')
    next_node = None
    for edge in edges:
        if edge.from_node == current_node and edge.to_node not in visited:
            if edge.weight < min_weight:
                min_weight = edge.weight
                next_node = edge.to_node
    return next_node

def find_next_node_price(current_node, visited, edges):
    min_price = float('inf')
    next_node = None
    for edge in edges:
        if edge.from_node == current_node and edge.to_node not in visited:
            if edge.is_toll and edge.price < min_price:
                min_price = edge.price
                next_node = edge.to_node
            elif not edge.is_toll and edge.price < min_price:
                min_price = edge.price
                next_node = edge.to_node
    return next_node

def greedy_tsp_weight(start_node, end_node, edges):
    current_node = start_node
    visited = set()
    path = []
    total_weight = 0
    total_price = 0

    while current_node != end_node:
        visited.add(current_node)
        path.append(current_node)
        next_node = find_next_node_weight(current_node, visited, edges)
        if next_node is None:
            return None, None, None  # Tidak ada jalur ke end_node

        for edge in edges:
            if edge.from_node == current_node and edge.to_node == next_node:
                total_weight += edge.weight
                if edge.is_toll:
                    total_price += edge.price
                break
        current_node = next_node

    path.append(end_node)
    return path, total_weight, total_price

def greedy_tsp_price(start_node, end_node, edges):
    current_node = start_node
    visited = set()
    path = []
    total_weight = 0
    total_price = 0

    while current_node != end_node:
        visited.add(current_node)
        path.append(current_node)
        next_node = find_next_node_price(current_node, visited, edges)
        if next_node is None:
            return None, None, None  # Tidak ada jalur ke end_node

        for edge in edges:
            if edge.from_node == current_node and edge.to_node == next_node:
                total_weight += edge.weight
                total_price += edge.price
                break
        current_node = next_node

    path.append(end_node)
    return path, total_weight, total_price

start_node = 1
end_node = 8

# Greedy TSP by weight
path_weight, total_weight, total_price_weight = greedy_tsp_weight(start_node, end_node, edges)
if path_weight:
    print("Greedy TSP by weight:")
    print("Path:", path_weight)
    print("Total weight:", total_weight)
    print("Total price:", total_price_weight)
else:
    print("No valid path found from", start_node, "to", end_node)
print()

Pling_optimal = []
#-----------------------------------------------------------------------------------------------------------------------------------
orang = 12
harga_per_liter = 12000

# Greedy by kapasitas
selected_mobil_kapasitas = greedy_mobil_by_kapasitas(mobil_list, orang)
print("Greedy by kapasitas:")
for mobil in selected_mobil_kapasitas:
    print(f"Nama: {mobil.nama}, Kapasitas: {mobil.kapasitas}, Biaya Sewa: {mobil.biaya_sewa}, Biaya Bahan Bakar: {mobil.biaya_bahan_bakar(total_weight, harga_per_liter)}")
print(f"Total Biaya: {total_biaya(selected_mobil_kapasitas, total_weight, harga_per_liter) + total_price_weight}\n")
Pling_optimal.append(total_biaya(selected_mobil_kapasitas, total_weight, harga_per_liter) + total_price_weight)

# Greedy by efisiensi bahan bakar
selected_mobil_efisiensi = greedy_mobil_by_efisiensi_bahan_bakar(mobil_list, total_weight, harga_per_liter)
print("Greedy by efisiensi bahan bakar:")
for mobil in selected_mobil_efisiensi:
    print(f"Nama: {mobil.nama}, Kapasitas: {mobil.kapasitas}, Biaya Sewa: {mobil.biaya_sewa}, Biaya Bahan Bakar: {mobil.biaya_bahan_bakar(total_weight, harga_per_liter)}")
print(f"Total Biaya: {total_biaya(selected_mobil_efisiensi, total_weight, harga_per_liter) + total_price_weight}\n")
Pling_optimal.append(total_biaya(selected_mobil_efisiensi, total_weight, harga_per_liter) + total_price_weight)

# Greedy by biaya sewa
selected_mobil_biaya_sewa = greedy_mobil_by_biaya_sewa(mobil_list, orang)
print("Greedy by biaya sewa:")
for mobil in selected_mobil_biaya_sewa:
    print(f"Nama: {mobil.nama}, Kapasitas: {mobil.kapasitas}, Biaya Sewa: {mobil.biaya_sewa}, Biaya Bahan Bakar: {mobil.biaya_bahan_bakar(total_weight, harga_per_liter)}")
print(f"Total Biaya: {total_biaya(selected_mobil_biaya_sewa, total_weight, harga_per_liter) + total_price_weight}\n")
Pling_optimal.append(total_biaya(selected_mobil_biaya_sewa, total_weight, harga_per_liter) + total_price_weight)

# Greedy by density (biaya sewa per penumpang)
BBM = mobil.biaya_bahan_bakar(total_weight, harga_per_liter)

selected_mobil_density = greedy_mobil_by_density(mobil_list, orang, BBM)
print("Greedy by density (biaya (sewa + bahan bakar) per penumpang):")
for mobil in selected_mobil_density:
    print(f"Nama: {mobil.nama}, Kapasitas: {mobil.kapasitas}, Biaya Sewa: {mobil.biaya_sewa}, Biaya Bahan Bakar: {mobil.biaya_bahan_bakar(total_weight, harga_per_liter)}")
print(f"Total Biaya: {total_biaya(selected_mobil_density, total_weight, harga_per_liter) + total_price_weight}\n")
Pling_optimal.append(total_biaya(selected_mobil_density, total_weight, harga_per_liter) + total_price_weight)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Greedy TSP by price
path_price, total_weight_price, total_price = greedy_tsp_price(start_node, end_node, edges)
if path_price:
    print("Greedy TSP by price:")
    print("Path:", path_price)
    print("Total weight:", total_weight_price)
    print("Total price:", total_price)
else:
    print("No valid path found from", start_node, "to", end_node)

print()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

orang = 12
harga_per_liter = 12000
BBM = mobil.biaya_bahan_bakar(total_weight_price, harga_per_liter)

# Greedy by kapasitas
selected_mobil_kapasitas = greedy_mobil_by_kapasitas(mobil_list, orang)
print("Greedy by kapasitas:")
for mobil in selected_mobil_kapasitas:
    print(f"Nama: {mobil.nama}, Kapasitas: {mobil.kapasitas}, Biaya Sewa: {mobil.biaya_sewa}, Biaya Bahan Bakar: {mobil.biaya_bahan_bakar(total_weight_price, harga_per_liter)}")
print(f"Total Biaya: {total_biaya(selected_mobil_kapasitas, total_weight_price, harga_per_liter) + total_price}\n")
Pling_optimal.append(total_biaya(selected_mobil_kapasitas, total_weight_price, harga_per_liter) + total_price)

# Greedy by efisiensi bahan bakar
selected_mobil_efisiensi = greedy_mobil_by_efisiensi_bahan_bakar(mobil_list, total_weight_price, harga_per_liter)
print("Greedy by efisiensi bahan bakar:")
for mobil in selected_mobil_efisiensi:
    print(f"Nama: {mobil.nama}, Kapasitas: {mobil.kapasitas}, Biaya Sewa: {mobil.biaya_sewa}, Biaya Bahan Bakar: {mobil.biaya_bahan_bakar(total_weight_price, harga_per_liter)}")
print(f"Total Biaya: {total_biaya(selected_mobil_efisiensi, total_weight_price, harga_per_liter)+ total_price}\n")
Pling_optimal.append(total_biaya(selected_mobil_efisiensi, total_weight_price, harga_per_liter)+ total_price)

# Greedy by biaya sewa
selected_mobil_biaya_sewa = greedy_mobil_by_biaya_sewa(mobil_list, orang)
print("Greedy by biaya sewa:")
for mobil in selected_mobil_biaya_sewa:
    print(f"Nama: {mobil.nama}, Kapasitas: {mobil.kapasitas}, Biaya Sewa: {mobil.biaya_sewa}, Biaya Bahan Bakar: {mobil.biaya_bahan_bakar(total_weight_price, harga_per_liter)}")
print(f"Total Biaya: {total_biaya(selected_mobil_biaya_sewa, total_weight_price, harga_per_liter)+ total_price}\n")
Pling_optimal.append(total_biaya(selected_mobil_biaya_sewa, total_weight_price, harga_per_liter)+ total_price)

# Greedy by density (biaya sewa per penumpang)
selected_mobil_density = greedy_mobil_by_density(mobil_list, orang, BBM)
print("Greedy by density (biaya (sewa + Bahan Bakar) per penumpang):")
for mobil in selected_mobil_density:
    print(f"Nama: {mobil.nama}, Kapasitas: {mobil.kapasitas}, Biaya Sewa: {mobil.biaya_sewa}, Biaya Bahan Bakar: {mobil.biaya_bahan_bakar(total_weight_price, harga_per_liter)}")
print(f"Total Biaya: {total_biaya(selected_mobil_density, total_weight_price, harga_per_liter) + total_price}\n")
Pling_optimal.append(total_biaya(selected_mobil_density, total_weight_price, harga_per_liter) + total_price)


#ngitung yg pling optimal
print(f"Maka solusi yang paling hemat adalah kombinasi yang menghasilkan total biaya: {min(Pling_optimal)}")

# Selesai pengukuran waktu
end_time = time.time()

# Hitung total waktu eksekusi
execution_time = end_time - start_time
print()
print(f"Total execution time: {execution_time} seconds")
