import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# PASO 2: DEFINIR LOS DATOS INICIALES DE NUESTRO PROBLEMA (PARÁMETROS)
# =============================================================================
N0 = 100       # Usuarios iniciales el Día 0
K = 10000      # Capacidad máxima del servidor
t = np.linspace(0, 24, 500)  # Tiempo de simulación: 24 meses (2 años)

# Las 3 tasas de crecimiento que definen cada comportamiento
r_baja = 0.15   # Caso de Baja Productividad (Estancamiento)
r_base = 0.40   # Caso de Crecimiento Normal (Orgánico)
r_alta = 0.90   # Caso de Alta Productividad (Viralización)

# =============================================================================
# PASO 3: PROGRAMAR LA FÓRMULA MATEMÁTICA LOGÍSTICA
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
# PASO 5: DIBUJAR LOS 3 GRÁFICOS INDEPENDIENTES (REQUISITO REGLAMENTARIO)
# =============================================================================
# Creamos una ventana ancha (18 pulgadas) para que quepan los 3 gráficos en una fila
plt.figure(figsize=(18, 5))

# --- GRÁFICO 1: CASO BAJA PRODUCTIVIDAD (IZQUIERDA) ---
# Subplot: 1 fila, 3 columnas, posición 1
plt.subplot(1, 3, 1)
plt.plot(t, usuarios_baja, color='red', linestyle=':', linewidth=2.5, label=f'Baja Prod. (r={r_baja})')
plt.axhline(y=K, color='black', linestyle='-.', alpha=0.5, label=f'Límite K={K}')
plt.title('Baja Productividad', fontsize=12, fontweight='bold')
plt.xlabel('Tiempo (Meses)')
plt.ylabel('Cantidad de Usuarios (N)')
plt.ylim(0, 11000)  # Mantiene la misma escala visual en todos los gráficos
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

# --- GRÁFICO 2: CASO CRECIMIENTO NORMAL (CENTRO) ---
# Subplot: 1 fila, 3 columnas, posición 2
plt.subplot(1, 3, 2)
plt.plot(t, usuarios_base, color='blue', linestyle='-', linewidth=2.5, label=f'Crecimiento Normal (r={r_base})')
plt.axhline(y=K, color='black', linestyle='-.', alpha=0.5)
plt.title('Crecimiento Orgánico', fontsize=12, fontweight='bold')
plt.xlabel('Tiempo (Meses)')
plt.ylabel('Cantidad de Usuarios (N)')
plt.ylim(0, 11000)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

# --- GRÁFICO 3: CASO ALTA PRODUCTIVIDAD (DERECHA) ---
# Subplot: 1 fila, 3 columnas, posición 3
plt.subplot(1, 3, 3)
plt.plot(t, usuarios_alta, color='green', linestyle='--', linewidth=2.5, label=f'Alta Prod. (r={r_alta})')
plt.axhline(y=K, color='black', linestyle='-.', alpha=0.5)
plt.title('Alta Productividad', fontsize=12, fontweight='bold')
plt.xlabel('Tiempo (Meses)')
plt.ylabel('Cantidad de Usuarios (N)')
plt.ylim(0, 11000)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

# Ajusta el espaciado para que no se superpongan los textos de los ejes
plt.tight_layout()

# Mostrar la ventana con las 3 gráficas independientes
plt.show()
