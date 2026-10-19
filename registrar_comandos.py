
import os
import json
import urllib.request
import urllib.error

APP_ID = "1561853843560734810"
TOKEN = os.environ["DISCORD_TOKEN"]

comando = {
    "name": "arbitragem",
    "description": "Arbitragens do Warframe",
    "type": 1,
    "integration_types": [0],
    "contexts": [0],
    "options": [
        {
            "type": 1,
            "name": "configurar",
            "description": "Escolher canal para avisos",
            "options": [
                {
                    "type": 7,
                    "name": "canal",
                    "description": "Canal de texto",
                    "required": True,
                    "channel_types": [0]
                }
            ]
        },
        {
            "type": 1,
            "name": "atual",
            "description": "Ver a Arbitragem atual"
        },
        {
            "type": 1,
            "name": "status",
            "description": "Ver canal configurado"
        },
        {
            "type": 1,
            "name": "desativar",
            "description": "Desativar avisos"
        }
    ]
}

url = f"https://discord.com/api/v10/applications/{APP_ID}/commands"

req = urllib.request.Request(
    url,
    data=json.dumps(comando).encode(),
    headers={
        "Authorization": f"Bot {TOKEN}",
        "Content-Type": "application/json"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=30) as response:
        print("Comando registrado com sucesso!")
        print("HTTP:", response.status)
except urllib.error.HTTPError as erro:
    print("Erro HTTP:", erro.code)
    print(erro.read().decode())
    raise
