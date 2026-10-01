import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# PASO 2: DEFINIR LOS DATOS INICIALES DE NUESTRO PROBLEMA (PARÁMETROS)
# =============================================================================
N0 = 100       # Usuarios iniciales
K = 10000      # Capacidad máxima del servidor
t = np.linspace(0, 24, 500)  # Tiempo de simulación: 24 meses

# Tasas de crecimiento para los 3 escenarios
r_baja = 0.15   # Caso de Baja Productividad
r_base = 0.40   # Caso de Crecimiento Normal
r_alta = 0.90   # Caso de Alta Productividad

# =============================================================================
# PASO 3: PROGRAMAR LA FÓRMULA MATEMÁTICA
# =============================================================================
def solucion_logistica(t, N0, K, r):
    numerator = K * N0
    denominator = N0 + (K - N0) * np.exp(-r * t)
    return numerator / denominator

# =============================================================================
# PASO 4: CALCULAR LOS RESULTADOS USANDO LA FUNCIÓN
# =============================================================================
usuarios_baja = solucion_logistica(t, N0, K, r_baja)
usuarios_base = solucion_logistica(t, N0, K, r_base)
usuarios_alta = solucion_logistica(t, N0, K, r_alta)

# =============================================================================
# PASO 5: DIBUJAR LOS GRÁFICOS (REQUISITO REGLAMENTARIO DE LA GUÍA: MÍNIMO 2)
# =============================================================================
plt.figure(figsize=(14, 5))

# --- GRÁFICO 1: COMPORTAMIENTO BASE ---
plt.subplot(1, 2, 1)
plt.plot(t, usuarios_base, color='blue', linewidth=2, label=f'Crecimiento Normal (r={r_base})')
plt.axhline(y=K, color='black', linestyle='-.', label=f'Límite del Servidor (K={K})')
plt.title('Gráfico 1: Adopción de Usuarios (Escenario Orgánico)')
plt.xlabel('Tiempo (Meses)')
plt.ylabel('Cantidad de Usuarios (N)')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

# --- GRÁFICO 2: COMPARACIÓN DE PRODUCTIVIDAD (ALTA VS BAJA) ---
plt.subplot(1, 2, 2)
plt.plot(t, usuarios_alta, color='green', linestyle='--', linewidth=2, label=f'Alta Productividad (r={r_alta})')
plt.plot(t, usuarios_baja, color='red', linestyle=':', linewidth=2, label=f'Baja Productividad (r={r_baja})')
plt.axhline(y=K, color='black', linestyle='-.')
plt.title('Gráfico 2: Análisis de Productividad (Límites y Tendencias)')
plt.xlabel('Tiempo (Meses)')
plt.ylabel('Cantidad de Usuarios (N)')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

plt.tight_layout()

# Mostrar la ventana con ambos gráficos independientes
plt.show()
