"""
Juego de Othello (Reversi)

El tablero es de 8x8. Las posiciones se indexan así:
  0  1  2  3  4  5  6  7
  8  9 10 11 12 13 14 15
 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31
 32 33 34 35 36 37 38 39
 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55
 56 57 58 59 60 61 62 63

Cada celda puede ser 0 (vacía), 1 (jugador 1) o -1 (jugador 2).

El estado es una tupla de 65 elementos: los primeros 64 son el tablero,
el elemento 64 indica si el turno anterior fue un pase (1) o no (0),
para poder detectar cuando ambos jugadores pasan y el juego termina.
"""

import juegos_simplificado as js
import minimax


DIRECCIONES = [(-1, -1), (-1, 0), (-1, 1),
               ( 0, -1),          ( 0, 1),
               ( 1, -1), ( 1, 0), ( 1, 1)]


def _fila(pos):
    return pos // 8


def _col(pos):
    return pos % 8


def _fichas_a_voltear(s, pos, jugador):
    """
    Devuelve la lista de posiciones a voltear si el jugador coloca
    una ficha en pos. Si la jugada no es válida, devuelve lista vacía.
    """
    if s[pos] != 0:
        return []
    rival = -jugador
    a_voltear = []
    fila, col = _fila(pos), _col(pos)

    for df, dc in DIRECCIONES:
        candidatos = []
        r, c = fila + df, col + dc
        while 0 <= r < 8 and 0 <= c < 8:
            idx = r * 8 + c
            if s[idx] == rival:
                candidatos.append(idx)
                r += df
                c += dc
            elif s[idx] == jugador:
                a_voltear.extend(candidatos)
                break
            else:
                break

    return a_voltear


class Othello(js.JuegoZT2):
    """
    Juego de Othello basado en JuegoZT2.
    """

    def inicializa(self):
        raise NotImplementedError("Por implementar")

    def jugadas_legales(self, s, j):
        raise NotImplementedError("Por implementar")

    def sucesor(self, s, a, j):
        raise NotImplementedError("Por implementar")

    def terminal(self, s):
        raise NotImplementedError("Por implementar")

    def ganancia(self, s):
        raise NotImplementedError("Por implementar")