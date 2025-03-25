from src.campo.service import Campo

input_casas = int(input('Digite a quantidade de casas: '))

campo = Campo()
campo.criar_campo(input_casas)
campo.ver_campo()
    