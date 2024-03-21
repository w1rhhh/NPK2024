# создание необходимых функций

def smoothstep(t): 
    return t * t * t * (t * (t * 6 - 15) + 10) # quintic
    # return -2 * t * t * t + 3 * t * t # bicube
    # return t

def noise(x, y, seed = 1):
    n = (x + y * 57)
    n = (n << 13) ^ n
    return (1.0 - (((n * (n * n * 15731 * seed + 789221) + 1376312589 * seed) & int(1073741824.0*1.8)) / 1073741824.0))

def interpolate(a, b, t): return a + (b - a) * t

def perlin(x, y, seed=0):
    # определение положение точки в "квадрате"
    X = int(x)
    Y = int(y)
    x -= X
    y -= Y
    X = X & 255
    Y = Y & 255

    # распределение шумового градиента
    n00 = noise(X, Y, seed)
    n01 = noise(X, Y + 1, seed)
    n10 = noise(X + 1, Y, seed)
    n11 = noise(X + 1, Y + 1, seed)

    # линейная интерполяция с кубическим сглаживаением
    i1 = smoothstep(interpolate(n00, n10, x))
    i2 = smoothstep(interpolate(n01, n11, x))
    return interpolate(i1, i2, y)

def print_array(arr):
    arr1 = list(map(list, zip(*arr)))
    for i in range(len(arr1)):
        k = len(max(list(map(str, arr1[i])),  key=len))
        arr1[i] = [f'{elem:{k}d}' for elem in arr1[i]]
    arr1 = list(map(list, zip(*arr1)))
    for row in arr1:
        print(*row)

# генерация шума перлина размерностью 20х20
seed = 9
width = 20
height = 20
octaves = 0.1
perlin_noise = [[perlin(x * octaves, y * octaves, seed) for x in range(width)] for y in range(height)]

# адекватная визуализация шума перлина
for row in range(len(perlin_noise)):
    for i in range(len(perlin_noise[row])):
        perlin_noise[row][i]  *= 10
        if perlin_noise[row][i] < 0: 
            perlin_noise[row][i] = (perlin_noise[row][i]/7)
        perlin_noise[row][i] = round(perlin_noise[row][i])

print_array(perlin_noise)
