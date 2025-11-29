from database.DB_connect import DBConnect
from model.compagnia import Compagnia
from model.hub import Hub
from model.spedizione import Spedizione
class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    def __init__(self):
        self.lista_visualizzazione = []
        self.esponi_valori_query()


    def elabora_sql_Compagnia(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM compagnia"
        cursor.execute(query)
        lista = []
        for row in cursor:
            compagnia = Compagnia(row["id"],row["codice"],row["nome"])
            lista.append(compagnia)
        cnx.close()
        cursor.close()
        return lista



    def elabora_sql_Hub(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM hub"
        cursor.execute(query)
        lista = []
        for row in cursor:
            hub = Hub(row["id"],row["codice"],row["nome"],row["citta"],row["stato"],row["latitudine"],row["longitudine"])
            lista.append(hub)
        cnx.close()
        cursor.close()
        return lista


    def elabora_sql_Spedizione(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM spedizione"
        cursor.execute(query)
        lista = []
        for row in cursor:
            spedizione = Spedizione(row["id"],row["id_compagnia"],row["numero_tracking"],row["id_hub_origine"],row["id_hub_destinazione"],row["data_ritiro_programmata"],row["distanza"],row["data_consegna"],row["valore_merce"])
            lista.append(spedizione)
        cnx.close()
        cursor.close()
        return lista



    def esponi_valori_query(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT id_hub_origine,id_hub_destinazione,SUM(valore_merce),COUNT(*) FROM spedizione  GROUP BY id_hub_origine, id_hub_destinazione"""
        cursor.execute(query)
        for row in cursor:
            self.lista_visualizzazione.append([row["id_hub_origine"],row["id_hub_destinazione"],row["SUM(valore_merce)"],row["COUNT(*)"]])
        cnx.close()
        cursor.close()

    def guadagno_medio_tratta(self,hub1,hub2):
        somma1= 0
        conto1 = 0
        for i in self.lista_visualizzazione:
            if i[0]==hub1.id and i[1]==hub2.id or i[0]==hub2.id and i[1]==hub1.id:
                somma1 += i[2]
                conto1 += i[3]
            else:
                pass
        return somma1,conto1












