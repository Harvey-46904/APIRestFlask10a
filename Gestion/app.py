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
    username=[]
    userid=[]
    usernombre=[]
    userapellido=[]
    useridenti=[]
    useremail=[]
    usercontra=[]
    usereda=[]
    tam=len(usuarios)
    for x in range(0,len(usuarios)):
        username.append(usuarios[x])
        userid.append(usuarios[x]['id'])
        usernombre.append(usuarios[x]['nombre'])
        userapellido.append(usuarios[x]['apellido'])
        useridenti.append(usuarios[x]['identificacion'])
        useremail.append(usuarios[x]['email'])
        usercontra.append(usuarios[x]['password'])
        usereda.append(usuarios[x]['edad'])
       
    return render_template('index.html',username=username,userid=userid,usernombre=usernombre,userapellido=userapellido,useridenti=useridenti,useremail=useremail,usercontra=usercontra,usereda=usereda,tam=tam)
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
@app.route('/usuarios_delete/<int:usuarios_id>',methods=['DELETE'])
def deleteuser(usuarios_id):
    users=[usuario for usuario in usuarios if usuario['id']==usuarios_id]
    if len(users)>0:
        usuarios.remove(users[0])
        return jsonify({"mensage":"dato eliminado"})
    
if __name__=='__main__':
    app.run(debug=True,port=4000)
