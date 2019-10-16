from flask import Flask,jsonify,template_rendered,render_template,request
from usuarios import usuarios
app=Flask(__name__)




@app.route('/usuarios',methods=['GET'])
def getusers():
    return jsonify(usuarios)
@app.route('/usuarios/<string:usuarios_id>')
def getuser(usuarios_id):
    usuarios_t=[usuario for usuario in usuarios if usuario['id']==usuarios_id]
    if (len(usuarios_t)>0):
        return jsonify({"usuario":usuarios_t[0]})
    else :
        return jsonify({"mensage":"usuario no encontrado"})
@app.route('/')
def menu():
    return render_template('index.html')
@app.route('/registro_usuarios',methods=['POST'])
def registro():
    n_usuario={
        "id":request.form['id'],
        "nombre":request.form['nombre'],
        "apellido":request.form['apellido'],
        "identificacion":request.form['identificacion'],
        "email":request.form['email'],
        "password":request.form['password'],
        "edad":request.form['edad']
    }
    usuarios.append(n_usuario)
    return jsonify({"usuarios":usuarios})

    
if __name__=='__main__':
    app.run(debug=True,port=4000)
