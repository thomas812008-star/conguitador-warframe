
import os
import json
import urllib.request
import urllib.error

# Configurações do Conguitador
APP_ID = "1561853843560734810"
TOKEN = os.environ["DISCORD_TOKEN"]

API_URL = (
    f"https://discord.com/api/v10/"
    f"applications/{APP_ID}/commands"
)

# Comandos do Discord
comando = {
    "name": "arbitragem",
    "description": "Arbitragens do Warframe com tiers",
    "type": 1,
    "integration_types": [0],
    "contexts": [0],
    "options": [
        {
            "type": 1,
            "name": "configurar",
            "description": "Escolher canal de notificações",
            "options": [
                {
                    "type": 7,
                    "name": "canal",
                    "description": "Canal que receberá as Arbitragens",
                    "required": True,
                    "channel_types": [0]
                }
            ]
        },
        {
            "type": 1,
            "name": "atual",
            "description": "Mostrar a Arbitragem atual"
        },
        {
            "type": 1,
            "name": "status",
            "description": "Verificar canal configurado"
        },
        {
            "type": 1,
            "name": "desativar",
            "description": "Desativar notificações"
        }
    ]
}

# Preparar requisição
dados = json.dumps(comando).encode("utf-8")

headers = {
    "Authorization": f"Bot {TOKEN}",
    "Content-Type": "application/json",
    "User-Agent": (
        "DiscordBot "
        "(https://github.com/thomas812008-star/"
        "conguitador-warframe, 1.0)"
    ),
    "Accept": "application/json"
}

requisicao = urllib.request.Request(
    API_URL,
    data=dados,
    headers=headers,
    method="POST"
)

# Registrar comandos
print("Registrando comandos do Conguitador...")

try:
    with urllib.request.urlopen(
        requisicao,
        timeout=30
    ) as resposta:

        resultado = json.loads(
            resposta.read().decode("utf-8")
        )

        print("Comandos registrados com sucesso!")
        print("HTTP:", resposta.status)
        print("Nome:", resultado.get("name"))
        print("ID:", resultado.get("id"))

except urllib.error.HTTPError as erro:
    print("Erro HTTP:", erro.code)

    corpo = erro.read().decode(
        "utf-8",
        errors="replace"
    )

    try:
        erro_json = json.loads(corpo)
        print(json.dumps(
            erro_json,
            indent=2,
            ensure_ascii=False
        ))
    except json.JSONDecodeError:
        print(corpo[:1000])

    raise SystemExit(1)

except Exception as erro:
    print("Erro ao registrar comandos:", erro)
    raise SystemExit(1)
