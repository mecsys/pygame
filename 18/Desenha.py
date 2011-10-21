from Fonte import Fonte
from Display import Display

class Desenha(Fonte, Display):
    """Class Desenha
    """
    # Attributes:
    __screen = None  # (Display) 
    __fonte = None  # (Fonte) 
    
    # Operations
    def desenhaScreen(self, ):
        """function desenhaScreen
        
        : 
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def setDesenha(self, screen, fonte):
        """function setDesenha
        
        screen: Display
        fonte: Fonte
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def initScreen(self):
        """function initScreen
        
        returns void
        """
        return None # should raise NotImplementedError()
    
    def desenhaTexto(self, texto, font, screen, heighty, tamanho, frente, fundo):
        """function desenhaTexto
        
        texto: string
        font: fonte
        screen: Display
        heighty: int
        tamanho: int
        frente: int
        fundo: 
        
        returns 
        """
        return None # should raise NotImplementedError()
    

