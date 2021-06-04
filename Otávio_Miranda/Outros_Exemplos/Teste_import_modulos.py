
# teste para importação de módulos de pastas acima
# para cada pasta acima acrescenta '../'

try:
    import sys
    import os
    
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../'
            )
        )
    )
except ImportError:
    pass


from pacote1.modulo1 import variavel1

variavel2 = 'variavel2'

print(variavel1)