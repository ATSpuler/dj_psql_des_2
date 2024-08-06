from.models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.all()
    resultado = []
    for tarea in tareas:
        tarea_data = {
            'id': tarea.id,
            'descripcion': tarea.descripcion,
            'estado': tarea.estado,
           'subtareas': []
        }
        sub_tareas = SubTarea.objects.filter(tarea=tarea)
        for sub_tarea in sub_tareas:
            tarea_data['subtareas'].append({
                'id': sub_tarea.id,
                'descripcion': sub_tarea.descripcion,
                'estado': sub_tarea.estado
            })
        resultado.append(tarea_data)
    return resultado

def crear_nueva_tarea(descripcion, estado):
    tarea = Tarea.objects.create(descripcion=descripcion, estado=estado)
    datos = recupera_tareas_y_sub_tareas()
    imprimir_en_pantalla(datos)
    return datos

def crear_sub_tarea(tarea_id, descripcion, estado):
    tarea = Tarea.objects.get(id=tarea_id)
    sub_tarea = SubTarea.objects.create(tarea=tarea, descripcion=descripcion, estado=estado)
    datos = recupera_tareas_y_sub_tareas()
    imprimir_en_pantalla(datos)
    return datos

def elimina_tarea(tarea_id):
    Tarea.objects.get(id=tarea_id).delete()
    datos = recupera_tareas_y_sub_tareas()
    imprimir_en_pantalla(datos)
    return datos

def elimina_sub_tarea(sub_tarea_id):
    SubTarea.objects.get(id=sub_tarea_id).delete()
    datos = recupera_tareas_y_sub_tareas()
    imprimir_en_pantalla(datos)
    return datos

def imprimir_en_pantalla(datos):
    for tarea in datos:
        print(f"[{tarea['id']}] {tarea['descripcion']}")
        for sub_tarea in tarea['subtareas']:
            print(f".... [{sub_tarea['id']}] {sub_tarea['descripcion']}")