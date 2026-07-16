import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Créer les données aléatoires
rng = np.random.default_rng(42)
data = rng.normal(loc=0.0, scale=1.0, size=(500, 3))

# 2. Scatter plot 3D
fig = plt.figure(figsize=(10, 10))
axis = fig.add_subplot(111, projection='3d')
axis.scatter(data[:, 0], data[:, 1], data[:, 2], c=np.arange(len(data)), cmap='plasma')
plt.show()

# 3. Moyennes des colonnes
mean_col0 = np.mean(data[:, 0])
mean_all = np.mean(data, axis=0)
print("Moyenne colonne 0:", mean_col0)
print("Moyennes de chaque colonne:", mean_all)

# 4. Écart-type des colonnes
std_col0 = np.std(data[:, 0])
std_all = np.std(data, axis=0)
print("Écart-type colonne 0:", std_col0)
print("Écart-types de chaque colonne:", std_all)

# 5-7. Normalisation
centered = data - mean_all
std = std_all
if np.any(std == 0):
    raise ValueError("Une colonne a un écart-type nul")
datanorm = centered / std

# 8. Transposée
transposed = datanorm.T

# 9. Covariance
covariance = transposed @ datanorm / datanorm.shape[0]
print("Shape covariance:", covariance.shape)
print("Covariance via np.cov:", np.cov(datanorm, rowvar=False).shape)

# 10. Valeurs propres et vecteurs propres
values, vectors = np.linalg.eigh(covariance)

# 11. Trier les vecteurs propres par valeurs propres décroissantes
idx = np.argsort(values)[::-1]
values = values[idx]
vectors = vectors[:, idx]

# 12. Matrice PCA
pca = vectors[:, :2]

# 13. Données projetées
projecteddata = datanorm @ pca

# 14. Scatter plot 2D des données projetées
plt.figure(figsize=(8, 8))
plt.scatter(projecteddata[:, 0], projecteddata[:, 1], cmap='plasma')
plt.xlabel('Composante 1')
plt.ylabel('Composante 2')
plt.title('Projection PCA')
plt.show()

