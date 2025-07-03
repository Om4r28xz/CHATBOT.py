from difflib import SequenceMatcher
from app.config.db_methods import * 
from app.utils.sinonimos import sinonimos_func
from app.utils.palabras import palabras_saludo, palabras_despedida
from app.utils.text_changer import normalize, reemplazar_sinonimos

async def buscar_respuesta(question: str) -> str:
    q = normalize(question)

    palabras = q.split()

    # Saludo sin pregunta
    if q in palabras_saludo and len(palabras) <= 3:
        saludo = await get_quick_response_by_type("saludo")
        if saludo:
            print(await save_message(question, saludo.contenido))
            return saludo.contenido

    # Despedida sin pregunta
    if q in palabras_despedida and len(palabras) <= 3:
        despedida = await get_quick_response_by_type("despedida")
        if despedida:
            await save_message(question, despedida.contenido)
            return despedida.contenido

    q = reemplazar_sinonimos(q, sinonimos_func)
    print(f"Pregunta normalizada: {q}")

    funcionalidades = await get_functionalities()
    historia = await get_story()
    expresiones = await get_expressions()
    best, score = None, 0

    def actualizar_mejor(item, texto_a_comparar):
        nonlocal best, score
        s = SequenceMatcher(None, q, texto_a_comparar).ratio()
        print(f"Comparando '{q}' con '{texto_a_comparar}': {s}")
        if s > score:
            best, score = item, s

    for item in funcionalidades:
        pregunta_base = reemplazar_sinonimos(normalize(item.pregunta), sinonimos_func)
        actualizar_mejor(item, pregunta_base)

    for item in historia:
        pregunta_base = reemplazar_sinonimos(normalize(item.pregunta), sinonimos_func)
        actualizar_mejor(item, pregunta_base)

    for item in expresiones:
        expresion_base = reemplazar_sinonimos(normalize(item.pregunta), sinonimos_func)
        actualizar_mejor(item, expresion_base)

    if score > 0.8:
        # coincidencia alta, responderle instakill
        if hasattr(best, 'descripcion'):
            respuesta = best.descripcion
        else:
            respuesta = f"Tienes que hacer: {best.forma_realizacion}"
        await save_message(question, respuesta)
        return respuesta

    if score > 0.5:
        # lo que mas se acerca a la pregunta
        if hasattr(best, 'descripcion'):
            respuesta = f"No encontré tu pregunta exacta (revisa que este correctamente escrota), pero esta te puede interesar: {best.pregunta}?\n\n{best.descripcion}"
        else: 
            respuesta = f"No encontré tu pregunta exacta (revisa que este correctamente escrota), pero esta te puede interesar: {best.pregunta}?\n\n{best.forma_realizacion}"
        await save_message(question, respuesta)
        return respuesta

    # si no encontro nada en la base de datos nub
    respuesta = "No entendí tu pregunta. Intenta con otras palabras."
    print(await save_message(question, respuesta))
    return respuesta