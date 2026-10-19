
import urllib.request
from datetime import datetime, timezone

URL = "https://browse.wf/arbys.txt"

def consultar_arbitragem():
    req = urllib.request.Request(
        URL,
        headers={"User-Agent": "Conguitador/1.0"}
    )

    with urllib.request.urlopen(req, timeout=30) as resposta:
        linhas = resposta.read().decode("utf-8-sig").splitlines()

    agora = int(datetime.now(timezone.utc).timestamp())
    missoes = []

    for linha in linhas:
        try:
            horario, node = linha.strip().split(",", 1)
            missoes.append((int(horario), node.strip()))
        except ValueError:
            continue

    atuais = [m for m in missoes if m[0] <= agora]

    if not atuais:
        raise RuntimeError("Arbitragem atual não encontrada")

    inicio, node = max(atuais)

    print("⚔️ CONGUITADOR — ARBITRAGEM")
    print("Nó:", node)
    print("Início UTC:", datetime.fromtimestamp(
        inicio, timezone.utc
    ).strftime("%d/%m/%Y %H:%M"))
    print("Fonte:", URL)

if __name__ == "__main__":
    consultar_arbitragem()
