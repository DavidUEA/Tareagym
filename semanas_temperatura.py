# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 15},
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
            {"day": "Lunes", "temp": 90},
            {"day": "Martes", "temp": 92},
            {"day": "Miércoles", "temp": 94},
            {"day": "Jueves", "temp": 91},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 85},
            {"day": "Domingo", "temp": 82}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 89},
            {"day": "Martes", "temp": 91},
            {"day": "Miércoles", "temp": 93},
            {"day": "Jueves", "temp": 90},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 84},
            {"day": "Domingo", "temp": 81}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 91},
            {"day": "Martes", "temp": 93},
            {"day": "Miércoles", "temp": 95},
            {"day": "Jueves", "temp": 92},
            {"day": "Viernes", "temp": 89},
            {"day": "Sábado", "temp": 86},
            {"day": "Domingo", "temp": 83}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 88},
            {"day": "Martes", "temp": 90},
            {"day": "Miércoles", "temp": 92},
            {"day": "Jueves", "temp": 89},
            {"day": "Viernes", "temp": 86},
            {"day": "Sábado", "temp": 83},
            {"day": "Domingo", "temp": 80}
        ]
    ]
]

for ciudad in temperaturas:
    for semana in ciudad:
        suma = 0
        for dia in semana:
            suma += dia['temp']
        print(suma)