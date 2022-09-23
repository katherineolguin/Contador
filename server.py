from flask import Flask, render_template, session, redirect 
app = Flask(__name__)
app.secret_key= "Que pasa perross"


@app.route('/')
def start():
    if 'count' in session: #Pregutando si existe count en session

        session ['count'] +=2
    else:
    
        session ['count'] =0 # si no existe inicializamos el contador en 0

    return render_template ('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.clear()		# borra todas las claves
    return redirect('/')
    # session.pop('key_name')		












if __name__=="__main__":
    app.run(debug=True)