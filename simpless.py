import re
import os

def separar_por_numeros(texto):
    padrao = r'(\d{10})'
    delimitadores = re.findall(padrao, texto)
    partes = re.split(padrao, texto)

    resultado = []
    for i in range(1, len(partes), 2):
        numero = delimitadores[(i - 1) // 2]
        conteudo = partes[i] + (partes[i + 1] if i + 1 < len(partes) else '')
        resultado.append((numero, conteudo.strip()))
    return resultado

def extrair_nome(conteudo):
    padrao_nome = r';\s*([^;=]+)'
    match = re.search(padrao_nome, conteudo)
    return match.group(1).strip() if match else "desconhecido"

def salvar_partes_como_arquivos(partes, nome_pasta):
    if not os.path.exists(nome_pasta):
        os.makedirs(nome_pasta)

        texto='pis;nome;administrador;matricula;rfid;codigo;senha;barras;digitais'  
    
    for numero, conteudo in partes:
        nome_arquivo = extrair_nome(conteudo).replace("_", " ").upper()
        caminho_arquivo = os.path.join(nome_pasta, f"{nome_arquivo}.txt")

        conteudo_completo = f"{texto}\n{conteudo}\n"
        
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo_completo)
        print(f"Arquivo salvo: {caminho_arquivo}")

def main():
    print("=== Separador de Texto por Números ===")
    texto = input("Digite ou cole o texto que deseja processar: ")
    nome_pasta = input("Digite o nome da pasta onde os arquivos serão salvos (padrão: 'Meus_arquivos'): ") or "Meus_arquivos"

    partes = separar_por_numeros(texto)

    if not partes:
        print("Nenhum número de 11 dígitos encontrado no texto.")
        return

    print(f"{len(partes)} partes identificadas. Salvando arquivos na pasta '{nome_pasta}'...")
    salvar_partes_como_arquivos(partes, nome_pasta)
    print("Processo concluído!")

if __name__ == "__main__":
    main()
