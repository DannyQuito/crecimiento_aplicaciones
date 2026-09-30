# =============================================================================
# PASO 1: IMPORTAR LAS HERRAMIENTAS (LIBRERÍAS)
# =============================================================================
# NumPy nos sirve para hacer cálculos matemáticos avanzados y manejar listas de números.
import numpy as np

# Matplotlib (específicamente pyplot) es la herramienta que nos permite dibujar los gráficos.
import matplotlib.pyplot as plt


# =============================================================================
# PASO 2: DEFINIR LOS DATOS INICIALES DE NUESTRO PROBLEMA (PARÁMETROS)
# =============================================================================
N0 = 100       # Cantidad de usuarios con los que la aplicación inicia el Día 0.
K = 10000      # Capacidad máxima del servidor. La curva no puede pasar de aquí.

# Creamos una lista de 500 puntos intermedios que van desde el mes 0 hasta el mes 24 (2 años).
# Esto sirve para que la línea del gráfico se vea curva y suave, no recta ni pixelada.
t = np.linspace(0, 24, 500)  

# ESCENARIO BASE: El crecimiento normal de la app de forma orgánica (tasa del 40%).
r_base = 0.4 

# ESCENARIO ALTERNATIVO: Modificamos el parámetro 'r' al 70% simulando una campaña publicitaria.
r_alternativo = 0.7  


# =============================================================================
# PASO 3: PROGRAMAR LA FÓRMULA MATEMÁTICA QUE RESOLVISTE A MANO
# =============================================================================
# Definimos una función personalizada en Python llamada 'solucion_logistica'
def solucion_logistica(t, N0, K, r):
    # Parte de arriba de la fracción de tu solución analítica: K multiplicado por N0
    numerator = K * N0
    
    # Parte de abajo de la fracción: N0 + (K - N0) multiplicado por e^(-r*t)
    # np.exp() es la forma en que Python escribe la función exponencial "e"
    denominator = N0 + (K - N0) * np.exp(-r * t)
    
    # La función nos devuelve el resultado de dividir el numerador entre el denominador
    return numerator / denominator


# =============================================================================
# PASO 4: CALCULAR LOS RESULTADOS USANDO LA FUNCIÓN
# =============================================================================
# Calculamos mes a mes cuántos usuarios hay en el Escenario Base
usuarios_base = solucion_logistica(t, N0, K, r_base)

# Calculamos mes a mes cuántos usuarios hay en el Escenario de Marketing
usuarios_alternativo = solucion_logistica(t, N0, K, r_alternativo)


# =============================================================================
# PASO 5: DIBUJAR LOS GRÁFICOS (REQUISITO DE LA GUÍA)
# =============================================================================
# Creamos un lienzo o ventana para los gráficos de 12 pulgadas de ancho por 5 de alto.
plt.figure(figsize=(12, 5))

# --- CONFIGURACIÓN DEL GRÁFICO 1 (IZQUIERDA) ---
# Le decimos a Python que dividiremos el lienzo en 1 fila y 2 columnas, y usaremos el espacio 1.
plt.subplot(1, 2, 1)

# Dibujamos la línea del Escenario Base en color azul y con un grosor de línea de 2.
plt.plot(t, usuarios_base, color='blue', linewidth=2, label=f'Escenario Base (r={r_base})')

# Dibujamos una línea horizontal roja y discontinua ('--') en el valor de K (10,000) para mostrar el límite.
plt.axhline(y=K, color='red', linestyle='--', label=f'Límite del Servidor (K={K})')

# Colocamos el título, y las etiquetas de los ejes X (tiempo) e Y (usuarios).
plt.title('Gráfico 1: Adopción de Usuarios (Escenario Base)')
plt.xlabel('Tiempo (Meses)')
plt.ylabel('Cantidad de Usuarios (N)')

# Activamos una cuadrícula de fondo punteada (':') y clarita (alpha=0.6) para leer mejor los datos.
plt.grid(True, linestyle=':', alpha=0.6)

# Mostramos el cuadro de leyendas que explica qué es cada línea según los 'label' anteriores.
plt.legend()


# --- CONFIGURACIÓN DEL GRÁFICO 2 (DERECHA) ---
# Nos cambiamos al espacio número 2 del lienzo (1 fila, 2 columnas, posición 2).
plt.subplot(1, 2, 2)

# Dibujamos la línea azul del Escenario Base otra vez para poder comparar.
plt.plot(t, usuarios_base, color='blue', linewidth=2, label=f'Base (r={r_base})')

# Dibujamos encima la línea del Escenario de Marketing en color verde y estilo punto-raya ('-.').
plt.plot(t, usuarios_alternativo, color='green', linewidth=2, linestyle='-.', label=f'Marketing (r={r_alternativo})')

# Dibujamos la misma línea horizontal roja del límite del servidor.
plt.axhline(y=K, color='red', linestyle='--')

# Ponemos los títulos y textos para este segundo gráfico.
plt.title('Gráfico 2: Análisis de Escenarios (Impacto de Parámetro)')
plt.xlabel('Tiempo (Meses)')
plt.ylabel('Cantidad de Usuarios (N)')

# Activamos la cuadrícula y las leyendas para este gráfico.
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

# Ajusta automáticamente los espacios entre los dos gráficos para que no se amontone el texto.
plt.tight_layout()

# Finalmente, le ordenamos a Google Colab que nos muestre el dibujo terminado en pantalla.
plt.show()