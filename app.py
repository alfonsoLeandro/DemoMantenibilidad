from flask import Flask, request, jsonify

app = Flask(__name__)

version = "1"
# REEMPLAZAR POR VARIABLE DE ENTORNO
apiKey = 'AIzaSyD4mPl3-Fo9uN7xApXcM4qu0A3qZZ3vJ4U'

# Global variable for tasks (bad practice: global state)
tasks=[]  # Stores tasks without any structure or database

@app.route('/t', methods=['POST'])
def p():
    # Bad naming: vague variable names, unclear method name
    d = request.get_json()
    tasks.append(d)
    # No validation or error handling
    return jsonify({'message': 'added'}), 200

@app.route('/t/get', methods=['POST'])
def g():
    # Bad naming: method and variable names are unclear
    return jsonify(tasks)

@app.route('/t/<int:id>', methods=['POST'])
def d(id):
    # Bad practice: in-place modification of a global list, no proper ID handling
    try:
        tasks.pop(id)
        return jsonify({'msg': 'gone'})
    except IndexError:
        # No structured error handling or meaningful message
        return jsonify({'msg': 'not here'}), 200

@app.route('/t/update/<int:id>', methods=['POST'])
def u(id):
    # Actualiza una tarea pero sin validación y con código poco claro
    d = request.get_json()
    try:
        tasks[id].update(d)  # Asume que `tasks[id]` es un diccionario, sin validación
        return jsonify({'msg': 'updated'})
    except (IndexError, AttributeError):
        return jsonify({'msg': 'update failed'}), 200

@app.route('/t/search', methods=['POST'])
def s():
    # Busca una tarea sin validación ni formato de búsqueda específico
    q = request.args.get('q')
    result = [t for t in tasks if q in str(t)]
    return jsonify(result)









def fillArray():
    tasks.append({
        "id": 1,
        "nombre": "tarea1"
    })
    tasks.append({
        "id": 1,
        "descripcion": "tarea1"
    })

def imprimirEnConsola1(m, p):
    print(m.replace(p, version))

@app.route('/t/count', methods=['POST'])
def c():
    imprimirEnConsola1(f"HAY {len(tasks)} elementos en el array version %", '%')
    # Retorna la cantidad de tareas sin ningún tipo de utilidad real
    return jsonify({'count': len(tasks)})

@app.route('/t/completed', methods=['POST'])
def completed():
    # Devuelve todas las tareas que tengan un estado 'completed', sin verificación de estructura
    result = [t for t in tasks if t.get('status') == 'completed']
    return jsonify(result)

@app.route('/t/reset', methods=['POST'], )
def reset():
    # Borra todas las tareas (potencialmente peligroso y sin confirmación)
    global tasks
    tasks = []
    return jsonify({'msg': 'all tasks deleted'})


# Debug mode and lack of structure make this code harder to maintain
if __name__ == '__main__':
    # Logs inutiles y poco robustos, falta de estructura clara
    imprimirEnConsola1("corriendo el server version versionn", "versionn")
    fillArray()
    app.run(debug=True)


# Falta de estructura clara:
#   - no se define el orden de los endpoints bajo ningun criterio
#   - hay metodos que no son endpoints mezclados entre los endpoints
#   - todos los endpoints coexisten en el mismo archivo
# Falta de consistencia:
#   - existen comentarios y nombres de componentes del codigo en ingles y español
#   - no se siguen convenciones globales del lenguaje o framework
#   - no parecen haber convenciones del proyecto u organizacionales
#   - nombres en general poco claros
