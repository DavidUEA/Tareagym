def calcula_temp(datos, ciudad, semana_inicio, semana_final):
    num_items = 0
    suma_temp = 0
    # Convertir en enteros
    semana_inicio = int (semana_inicio)
    semana_final = int (semana_final)

    # Ver si la ciudad y las semanas están dentro del rango
    if ciudad < len (datos):
        if semana_inicio >= 0 and semana_final < len (datos[ciudad]):
            for i in range (semana_inicio, semana_final + 1):
                for dia in datos[ciudad][i]:
                    suma_temp += dia['temp']
                    num_items += 1
                    print (dia)

            if num_items > 0:
                promedio = suma_temp / num_items
                return promedio
            else:
                return "No se encontraron datos para las semanas especificadas."
        else:
             return "Las semanas especificadas están fuera de rango."
    else:
        return "La ciudad especificada está fuera de rango."


# Crer la matriz o diccionario de ciudades y temperaturas
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "lunes", "temp": 12},
            {"day": "martes", "temp": 15},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 17}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 13}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 13},
            {"day": "Martes", "temp": 11},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 20},
            {"day": "Domingo", "temp": 19}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 13},
            {"day": "Domingo", "temp": 15}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 17}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 13},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 12},
            {"day": "Domingo", "temp": 18}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 15}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 18}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 24}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 33}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 31}
        ]
    ]
]
# ingreso de datos
ciudad = int (input ("Ingrese el número de la ciudad (0, 1, 2, etc.): "))
semana_inicio = input ("Ingrese semana de inicio: ")
semana_final = input ("Ingrese semana final: ")

# Llamada a función para los calculos
promedio_ca = calcula_temp (temperaturas, ciudad, semana_inicio, semana_final)
print ("El promedio de temperaturas es:", promedio_ca)