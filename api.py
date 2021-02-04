#Flask é para fazer gerenciamento de rotas, e iniciar o servidor
#render_tamplate busca um codigo html dentro da basta render_template

from flask import Flask, render_template, request

#O segundo parametro dentro de Flask é para definir o diretorio padrão onde o template_folder vai buscar a pagina html
app = Flask(__name__, template_folder="./src/views")

@app.route("/", methods=["GET", "POST"])
def home():
    if (request.method == "GET"):
        return render_template("index.html")
    else:
        if (request.form['num1'] != "" and request.form["num2"] != ""):
            num1 = request.form["num1"]
            num2 = request.form["num2"]
            opc = request.form["opc"]

            if (opc == "soma"):
                soma = int(num1) + int(num2)
                return { #o retorno da soma está em json, os demais não
                    "Resultado": str(soma)
                }
            elif (opc == "subt"):
                subt = int(num1) - int(num2)
                return str(subt) 

            elif (opc == "mult"):
                mult = int(num1) * int(num2)
                return str(mult)

            elif (opc == "divi"):
                divi = int(num1) // int(num2)
                return str(divi)

        else:
            return "informe os números"

@app.errorhandler(404)
def not_found(error):
    return render_template("error.html")

app.run(port=4000, debug=True)#PODE RECEBER A PORTA ONDE VAI RODAR - OPCINAL, E RECEBE DEBUG=TRUE - OPCINAL, PARA O SERVIDOR ATUALIZAR SEM MATAR O PROCESSO.