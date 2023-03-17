
class BlackJack:
    def _init_(self, apuesta: int):
        self.apuesta = apuesta

    def registrar_jugador(self, nombre):
        pass

    def iniciar_juego(self, apuesta):
        pass

    def seleccionar_jugada(self, apuesta):
        pass

    def remover_fichas(self, fichas):
        pass

    def agregar_fichas(self, fichas):
        pass

    def nueva_partida(self) -> bool:
        pass

    def anunciar_ganador(self):
        pass

    def anunciar_perdedor(self):
        pass

    def anunciar_empate(self):
        pass

    def finalizar_juego(self) -> bool:
        pass

class Jugador:
    def __init__(self, fichas: int, nombre: str):
        self.fichas = fichas
        self.nombre = nombre

    def inicializar_mano(self, cartas):
        pass

class Carta:
    def __init__(self, pinta: str, valor: str):
        self.pinta = pinta
        self.valor = valor
        self.tapado = bool


class Baraja:
    def __init__(self):
        pass

    def revolver(self):
        pass

    def repartir_carta(self, tapada: bool) -> Carta:
        pass


class Casa:
    def __init__(self):
        pass

    def inicializar_mano(self, cartas):
        pass


class Mano:
    def __init__(self, cartas):
        self.cartas = cartas

    def valor_mano(self, cartas):
        pass

    def comparar_manos(self, cartas):
        pass

    def destapar_oculta(self, cartas):
        pass

    def es_blackjack(self) -> bool:
        pass








