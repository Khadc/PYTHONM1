import numpy as np
import timeit

l1 = list(range(10000))
l2 = list(range(10000))
a1 = np.array(range(10000))
a2 = np.array(range(10000))

print("Liste Python:", timeit.timeit("[l1[i] + l2[i] for i in range(10000)]", globals=globals(), number=100))
print("map + lambda:", timeit.timeit("list(map(lambda x, y: x + y, l1, l2))", globals=globals(), number=100))
print("Tableau NumPy:", timeit.timeit("a1 + a2", globals=globals(), number=100))