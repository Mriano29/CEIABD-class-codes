# crear_documentos.py — genera dos archivos .txt en tu carpeta local
doc1 = """MANUAL DE EMPLEADO — TECHCORP S.L.
VACACIONES Y PERMISOS
Los empleados tienen derecho a 23 dias laborables de vacaciones al anyo.
Las vacaciones deben solicitarse con 15 dias de antelacion en el portal de RRHH.
En el primer anyo los dias se calculan de forma proporcional a la incorporacion.
Los permisos por enfermedad requieren justificante medico a partir del tercer dia.
HORARIO Y TELETRABAJO
El horario habitual es de 9:00 a 18:00 con una hora para comer.
Existe flexibilidad de entrada entre las 8:00 y las 10:00.
El teletrabajo esta permitido hasta 3 dias por semana con aprobacion del responsable.
Los viernes se puede salir a las 15:00 en julio y agosto.
EQUIPOS Y ACCESOS
Cada empleado recibe un portatil al incorporarse.
Las solicitudes de software se gestionan a traves de helpdesk@techcorp.es
El acceso a sistemas de produccion requiere aprobacion del CTO.
FORMACION
Cada empleado tiene un presupuesto anual de 1.500 euros para formacion externa.
Las certificaciones tecnicas aprobadas se reembolsan al 100%."""
doc2 = """POLITICA DE GASTOS — TECHCORP S.L.
DIETAS Y DESPLAZAMIENTOS
Los viajes de trabajo deben aprobarse con 48 horas de antelacion por el responsable.
Los billetes de avion se reservan a traves del portal de viajes corporativo.
La dieta diaria maxima en territorio nacional es de 45 euros.
Los desplazamientos en vehiculo propio se reembolsan a 0.26 euros por kilometro.
MATERIAL Y EQUIPAMIENTO
Los gastos de material de oficina hasta 50 euros no requieren aprobacion previa.
Los gastos superiores a 50 euros deben justificarse con factura y aprobacion del CTO.
El software de pago requiere siempre aprobacion del departamento de IT.
FORMACION EXTERNA
Las facturas de formacion deben presentarse en el portal de RRHH en los 30 dias siguientes.
Los cursos no aprobados previamente no son reembolsables aunque esten dentro del presupuesto.
La asistencia a conferencias requiere justificacion de relevancia para el puesto."""
with open('manual_empleado.txt', 'w', encoding='utf-8') as f:
    f.write(doc1)   
with open('politica_gastos.txt', 'w', encoding='utf-8') as f:
    f.write(doc2)
print('Archivos creados: manual_empleado.txt y politica_gastos.txt')
print('Subelos ahora a Azure Blob Storage (seccion 7.3)')