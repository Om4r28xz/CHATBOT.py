import re, unicodedata

def normalize(texto: str) -> str:
    texto = unicodedata.normalize('NFD', texto)
    texto = texto.encode('ascii', 'ignore').decode('utf-8')
    texto = re.sub(r'[^a-zA-Z0-9\s]', '', texto)
    texto = texto.lower().strip()

    return texto

def reemplazar_sinonimos(texto, sinonimos):
    for clave, lista in sinonimos.items():
        for palabra in lista:
            texto = re.sub(r'\b{}\b'.format(re.escape(palabra)), clave, texto)
    return texto