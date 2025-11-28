from database.DB_connect import DBConnect
from model.compagnia import Compagnia
from model.hub import Hub
from model.spedizione import Spedizione
class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    def __init__(self):
        self.lista_compagnia = []
        self.lista_hub = []
        self.lista_spedizioni = []

    def elabora_sql_Compagnia(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM compagnia"
        cursor.execute(query)
        for row in cursor:
            compagnia = Compagnia(row["id"],row["codice"],row["nome"])
            self.lista_compagnia.append(compagnia)
        return self.lista_compagnia

    def elabora_sql_Hub(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM hub"
        cursor.execute(query)
        for row in cursor:
            hub = Hub(row["id"],row["codice"],row["nome"],row["citta"],row["stato"],row["latitudine"],row["longitudine"])
            self.lista_hub.append(hub)
        return self.lista_hub

    def elabora_sql_Spedizione(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM spedizione"
        cursor.execute(query)
        for row in cursor:
            spedizione = Spedizione(row["id"],row["id_compagnia"],row["numero_tracking"],row["id_hub_origine"],row["id_hub_destinazione"],row["data_ritiro_programmata"],row["distanza"],row["data_consegna"],row["valore_merce"])
            self.lista_spedizioni.append(spedizione)
        return self.lista_spedizioni

    def guadagno_medio_tratta(self,hub1,hub2):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT id_hub_origine,id_hub_destinazione,SUM(valore_merce),COUNT(*) FROM spedizione WHERE id_hub_destinazione = %s AND id_hub_origine = %s GROUP BY id_hub_origine, id_hub_destinazione"""
        cursor.execute(query,(hub2,hub1))
        somma1= 0
        conto1 = 0
        for row in cursor:
            somma1 = row["SUM(valore_merce)"]
            conto1 = row["COUNT(*)"]
        query2 = """SELECT id_hub_origine,id_hub_destinazione,SUM(valore_merce),COUNT(*) FROM spedizione WHERE id_hub_destinazione = %s AND id_hub_origine = %s GROUP BY id_hub_origine, id_hub_destinazione"""
        somma2 = 0
        conto2 = 0
        cnx.close()
        cursor.close()
        cursor2 = cnx.cursor(dictionary=True)
        cursor2.execute(query2, (hub1, hub2))
        for row in cursor2:
            somma2 = row["SUM(valore_merce)"]
            conto2 = row["COUNT(*)"]
        cnx.close()
        cursor2.close()
        return somma1+somma2,conto1+conto2











