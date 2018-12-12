motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('bimota')
print(motorcycles)
motorcycles.insert(0,'vespa')
print(motorcycles)
del motorcycles[0]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(f"removed: {popped_motorcycle}")
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)