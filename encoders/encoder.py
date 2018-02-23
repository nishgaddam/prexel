from abc import ABCMeta, abstractmethod
#abc - abstract base class
#Basically Encoder class is an interface, we cannot create an instance of it, only use it as a superclass
#AN interface is a template that tells your class how to behave
class Encoder(metaclass=ABCMeta):
    @abstractmethod
    def generate(self, diagram):
        """ Generate a output from the supplied diagram"""

#By writing the @abstractmethod we are instructing the preety_print, source_code and xmi to compulsorily require a generate class         