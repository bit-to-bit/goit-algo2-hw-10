import random
import time
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(2000000)

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

if __name__ == '__main__':
    sizes = [10000, 50000, 100000, 500000]
    randomized_times = []
    deterministic_times = []

    for size in sizes:
        rand_time_sum = 0
        det_time_sum = 0
        
        for _ in range(5):
            arr = [random.randint(0, 1000000) for _ in range(size)]
            
            arr_copy1 = arr.copy()
            start_time = time.time()
            randomized_quick_sort(arr_copy1)
            rand_time_sum += (time.time() - start_time)
            
            arr_copy2 = arr.copy()
            start_time = time.time()
            deterministic_quick_sort(arr_copy2)
            det_time_sum += (time.time() - start_time)
            
        avg_rand = rand_time_sum / 5
        avg_det = det_time_sum / 5
        randomized_times.append(avg_rand)
        deterministic_times.append(avg_det)
        
        print(f"Розмір масиву: {size}")
        print(f"   Рандомізований QuickSort: {avg_rand:.4f} секунд")
        print(f"   Детермінований QuickSort: {avg_det:.4f} секунд\n")
        
    plt.plot(sizes, randomized_times, label='Рандомізований QuickSort', marker='o')
    plt.plot(sizes, deterministic_times, label='Детермінований QuickSort', marker='s')
    plt.xlabel('Розмір масиву')
    plt.ylabel('Середній час виконання (секунди)')
    plt.title('Порівняння рандомізованого та детермінованого QuickSort')
    plt.legend()
    plt.grid(True)
    plt.savefig('D:\\Education\\GoIT\\Neoversity\\Tier1\\Algorithms2\\hw-10\\goit-algo2-hw-10\\docs\\Графік_результат.png')
    plt.show()
