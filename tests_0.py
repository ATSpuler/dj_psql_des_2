from desafio_adl.models import Tarea, SubTarea
from desafio_adl.services import *

tarea = Tarea(descripcion='Mi tarea', estado='Pendiente')
tarea.save()
print(tarea.id)
print(tarea.descripcion)
print(tarea.estado)

crear_sub_tarea(tarea.id, 'Nueva sub-tarea', 'Pendiente')
elimina_tarea(tarea.id)
elimina_sub_tarea(sub_tarea.id)
imprimir_en_pantalla(recupera_tareas_y_sub_tareas())
