# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 10:53:31 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""

colores = ['Blanco', 'Azul', 'Rojo', 'Amarillo', 'Verde', 'Celeste', 'Fucsia']

# a = colores[1:5:3]
# print(a)
for i in range(0, len(colores)):
    if (i == 1 or i == 4):  # Extraemos el 2do y 4to elemento de la lista (NO INDICES)
        print(colores[i])
