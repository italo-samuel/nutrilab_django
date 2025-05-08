from django.contrib.messages import constants
from django.contrib import messages


def valida_numerico(request, peso, altura, gordura , musculo, hdl, ldl, colesterol_total, trigliceridios):
    if not peso.isnumeric():
        messages.add_message(request, constants.ERROR, 'Insira um peso válido!')
        return False
    if not altura.isnumeric():
        messages.add_message(request, constants.ERROR, 'Insira uma altura válida!')
        return False
    if not gordura.isnumeric():
        messages.add_message(request, constants.ERROR, 'Insira um valor válido em gordura!')
        return False
    if not musculo.isnumeric():
        messages.add_message(request, constants.ERROR, 'Insira um valor válido em musculo!')
        return False
    if not hdl.isnumeric():
        messages.add_message(request, constants.ERROR, 'Insira um hdl válido!')
        return False
    if not ldl.isnumeric():
        messages.add_message(request, constants.ERROR, 'Insira um ldl válido!')
        return False
    if not colesterol_total.isnumeric():
        messages.add_message(request, constants.ERROR, 'Insira um colesterol válido!')
        return False
    if not trigliceridios.isnumeric():
        messages.add_message(request, constants.ERROR, 'Insira um trigliceridio válido!')
        return False
    return True