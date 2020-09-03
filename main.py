from fastapi import FastAPI

DataBase = {
    "estabelecimento": {
        "nome": "Nosso Restaurante de Todo Dia LTDA",
        "cnpj": "45.283.163/0001-67",
        "dono": "Fabio I.",
        "telefone": "11909000300",
    },
    "recebimentos": [
    ],
    "total_recebido":[

    ]
}

def cpf(cpf:str):
    cpf_novo = cpf.replace('.','').replace('-','').replace('/','')
    if len(str(cpf_novo)) == 11 or len(str(cpf_novo)) == 14:
        return True


new_tranci= {
    "estabelecimento": "45.283.163/0001-67",
    "cliente": "094.214.930-01",
    "valor": 590.01,
    "descricao": "Almoço em restaurante chique pago via Shipay!"
}


D_L():
    DataBase["recebimentos"].append(new_tranci)
    DataBase["total_recebido"] + new_tranci["valor"]

app = FastAPI()

@app.post("/api/v1/transacao")
async def root():
    return D_L()


@app.get("/")
async def root_():
    return (DataBase)
