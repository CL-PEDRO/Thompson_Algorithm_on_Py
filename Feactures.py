
class Estado:
    def __init__(self):
        self.transiciones = {}  # Transiciones a otros estados
        self.isStateFinal = False
        self.isStateInitial = False
        self.number= None
    
    def agregar_transicion(self, simbolo, estado):
        if simbolo not in self.transiciones:
            self.transiciones[simbolo] = []
        self.transiciones[simbolo].append(estado)

class AFND:
    def __init__(self, inicial, final):
        self.inicial = inicial
        self.final = final



contador = -1  

def enumerateOfNodos(state):
    if not state: 
        return 
    
    if state.isStateFinal:  
        return
    
    global contador
    if state.number is None:  
        contador += 1
        state.number = contador  
    
    for currentState in state.transiciones.values():
        if isinstance(currentState, list):
            # Si el valor es una lista, iteramos sobre los estados dentro de la lista
            for subState in currentState:
                enumerateOfNodos(subState)  # Llama recursivamente para cada estado
        else:
            # Si el valor es un solo estado, llama la función recursivamente para ese estado
            enumerateOfNodos(currentState)


    



def makeCaseBase(LetterToTransition):
    
    NewCaseBase = AFND(Estado(),Estado())
    
    if NewCaseBase:
        
        NewCaseBase.inicial.transiciones[LetterToTransition] = NewCaseBase.final
        return NewCaseBase
    
    return None

def baseCase(ArrayLetrasOperandos):
    
    
    
    ArrayLetrasOperandosModificados = [] 
    
    for i,signo in enumerate(ArrayLetrasOperandos):
        
        if signo.isalpha():
            ArrayLetrasOperandosModificados.append(makeCaseBase(signo))
        else:
            ArrayLetrasOperandosModificados.append(ArrayLetrasOperandos[i])
            
    return ArrayLetrasOperandosModificados        
                        
#------------------------------PARSER
precedencia = {
    '*': 4,
    '+': 4,
    '?': 4,
    '.': 3, 
    '|': 2
}

def parser(expresion):
    pila_operadores = []
    salida = []
    
    
    for simbolo in expresion:
        if simbolo.isalnum():  # Si es un operando del alfabeto :
            salida.append(simbolo)
        elif simbolo == '(':
            pila_operadores.append(simbolo)
        elif simbolo == ')':
            while pila_operadores and pila_operadores[-1] != '(':
                salida.append(pila_operadores.pop())
            pila_operadores.pop()  # Eliminar el '('
        else:  # Es un operador del dicioniario 
            while (pila_operadores and pila_operadores[-1] != '(' and
                   precedencia[pila_operadores[-1]] >= precedencia[simbolo]):
                salida.append(pila_operadores.pop())
            pila_operadores.append(simbolo)
    
    
    while pila_operadores:
        salida.append(pila_operadores.pop())
    
    return ''.join(salida)

#------------------------------PARSER END


def agregaPunto(expresionR): 
    resultado = ""
    j = 0
    i = 0
    tam = len(expresionR)
    
    expre = [' '] * (tam +1) 
    
    while j < len(expresionR):
    
        expre[j] = expresionR[j]
        j = j+1
   
    while i < len(expresionR):
        expresion = expresionR[i]
             
        # Salta los caracteres especiales
        if expresion in ('(', '|'):
            resultado += expresion
            i += 1
            continue  
        # Si encuentra 'L' o 'l' al inicio de 'Letra'
        if expresion in ('L', 'l'):
            if comprobarLetra(expresionR[i:]):  # Verificar si comienza con "letra"
                if expre[i+5] in ( ')', '+', '*', '|', '?',' '):
                    resultado += "Letra"
                    i += 5
                    continue 
                else:
                    resultado += "Letra"  # Agregar "Letra" completo
                    resultado += '.'  # Insertar un punto después
                    i += 5  # Saltar el resto de "Letra"
                    continue
        # Si encuentra 'D' o 'd' al inicio de 'Digito'
        elif (expresion == 'D' or expresion == 'd'):
            if comprobarDigito(expresionR[i:]):  # Verificar si comienza con "digito"
                if expre[i+6] in ('(', ')', '+', '*', '|', '?'):
                    resultado += "Digito" 
                    i += 6
                    continue 
                else:
                    resultado += "Digito"  # Agregar "Digito" completo
                    resultado += '.'  # Insertar un punto después
                    i += 6  # Saltar el resto de "Digito"
                    continue
        
        # Si es una letra o digito no verificado, agregar el caracter actual
        if expre[i+1] in (')', '+', '*', '|', '?'):
            resultado += expresion
        else:
            resultado += expresion
            resultado += '.'  # Insertar un punto después de cada letra
        i += 1  # Avanza al siguiente caracter
        
    resultado = list(resultado.rstrip('.'))
    
    return resultado

def comprobarLetra(ExpresionR):
    if ExpresionR[0]== 'l':
        return ExpresionR.startswith("letra") 
    else:
        return ExpresionR.startswith("Letra")
    
def comprobarDigito(ExpresionR):
    
    if ExpresionR[0]== 'd':
        return ExpresionR.startswith("digito") 
    else:
        return ExpresionR.startswith("Digito")
    