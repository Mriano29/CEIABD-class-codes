semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

result = {i: semana[i] for i in range(len(semana)) if i % 2 == 0}

print(result)