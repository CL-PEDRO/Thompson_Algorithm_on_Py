
#------------------------------PARSER

precedencia = {
    '*': 4,
    '+': 4,
    '?': 4,
    '.': 3, 
    '|': 2
}



def makeCaseBase(LetterToTransition):
    
    NewCaseBase = AFND(Estado(),Estado())
    
    if NewCaseBase:
        
        NewCaseBase.inicial.transiciones(f"{LetterToTransition}") = NewCaseBase.final
        return NewCaseBase
    
    return None



def baseCase(ArrayLetrasOperandos):
    
    
    
    ArrayLetrasOperandosModificados = [] * (len(ArrayLetrasOperandos) + 1 )
    
    for i,signo in enumerate(ArrayLetrasOperandos):
        if signo.isalpha():
            ArrayLetrasOperandosModificados[i] = makeCaseBase(signo)
        else:
            ArrayLetrasOperandosModificados[i] = ArrayLetrasOperandos[i]
    
                    
        
        
    
    



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



def Creacion(self,expresionParser):
    
    pila = []
    
    for valor in expresionParser:
        if valor.isalnum():  # Si es un operando (carácter del alfabeto) :d
            pila.append(valor)
        elif valor == "*":
            pass
            kleen(pila.pop())
        elif valor == "+":
            pass
        elif valor == "?":
            pass
        elif valor == ".":
            pass
        elif valor == "|":
            pass
        
            
            
def kleen(self, afn1):
    
    afn3 =AFND(Estado(),Estado())
    
    afn3.inicial.agregar_transicion("e",afn1.inicial)
    afn3.inicial.agregar_transicion("e",afn3.final)
    
    afn1.final.agregar_transicion("e",afn3.final)
    afn1.final.agregar_transicion("e",afn1.inicial)
    
    
    return afn3
    
    
    
def opcional(self, afn1):
    
    afn3 =AFND(Estado(),Estado())
    
    afn3.inicial.agregar_transicion("e",afn1.inicial)
    afn3.inicial.agregar_transicion("e",afn3.final)
    afn1.final.agregar_transicion("e",afn3.final)
     
    return afn3    

def positiva(self, afn1):
    
    afn3 =AFND(Estado(),Estado())
    
    afn3.inicial.agregar_transicion("e",afn1.inicial)
    
    afn1.final.agregar_transicion("e",afn3.final)
    afn1.final.agregar_transicion("e",afn1.inicial)
     
    return afn3    
    
    
    
    
def concatenacion(A1,A2):
    
    for transicion in A2.final.transiciones:
        A1.final.transiciones.append(transicion)

    A1.final = A2.final
    
    return A1

def union(A1,A2):
    
    A3 = AFND(Estado(),Estado())
    
    if A3:
        A3.inicial.transiciones.append()
    
    pass    
    
    
    

class Estado:
    def __init__(self):
        self.transiciones = {}  # Transiciones a otros estados
        self.epsilon = []  # Transiciones epsilon
    
    def agregar_transicion(self, simbolo, estado):
        if simbolo not in self.transiciones:
            self.transiciones[simbolo] = []
        self.transiciones[simbolo].append(estado)

# Clase que representa un autómata finito no determinista (AFND)
class AFND:
    def __init__(self, inicial, final):
        self.inicial = inicial
        self.final = final



def concatenacion(self,afnd1,afnd2):
    
    afnd1.final = afnd2.inicial
    return AFND(afnd1.inicial,afnd2.final)
    
