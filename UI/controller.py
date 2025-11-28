import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        valore = self._view.guadagno_medio_minimo.value
        self._model.costruisci_grafo(valore)
        if type(valore) == str or type(valore) == int:
            try:
                valore = int(valore)
                self._view.lista_visualizzazione.controls.append(ft.Text(self._model.get_num_nodes()))
                self._view.lista_visualizzazione.controls.append(ft.Text(self._model.get_num_edges()))
                self._view.update()
                for i in self._model.get_all_edges():
                    self._view.lista_visualizzazione.controls.append(ft.text(i))
                self._view.update()

            except ValueError:
                self._view.show_alert("attenzione inserire numero e non valore lettarale")





