from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()
        self.Dao = DAO()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        lista_hub = self.Dao.elabora_sql_Hub()
        for hub in lista_hub:
            self.G.add_node(hub.nome)
        lista = []
        for hub in lista_hub:
            for hub2 in lista_hub:
                if (hub,hub2) not in lista and (hub2,hub) not in lista:
                    somma,conto=self.Dao.guadagno_medio_tratta(hub,hub2)
                    lista.append((hub,hub2))

                    if somma==0 or conto == 0:
                        pass
                    else:
                        guadagno_medio= somma/conto
                        if guadagno_medio >= int(threshold):
                            self.G.add_edge(hub.nome,hub2.nome, weight = guadagno_medio)

                        else:
                            pass

    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        return self.G.number_of_edges()

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        lista_hub = self.Dao.elabora_sql_Hub()
        return len(lista_hub)




