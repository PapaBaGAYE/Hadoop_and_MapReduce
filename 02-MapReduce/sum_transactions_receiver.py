from mrjob.job import MRJob
from mrjob.step import MRStep

class Sum_transactions_receiver(MRJob):  
    def steps(self):
        """Création d'une première méthode contenant les étapes à réaliser.
           On commence par une étape de mapping puis une étape de reduce"""
        return [
            MRStep(mapper = self.mapper_transactions_receiver,
                   reducer = self.reducer_transactions_receiver)
        ]
    
    def mapper_transactions_receiver(self, _, line):
        """Cette méthode contient le code pour réaliser l'étape de mapping.
           La sortie obtenue lors de cette étape est une liste 
           contenant des clés et des valeurs associés. """
        agency_id,account_sender_name,country_sender,\
        account_receiver_name,country_receiver,amount,\
        payment_type,datetime_timestamp = line.split(',')
        if amount != 'amount':
            yield (account_receiver_name, int(amount))
    
    def reducer_transactions_receiver(self, key, values):
        """Cette méthode contient le code pour réaliser l'étape de reducing.
         La sortie obtenue est le résultat 
         d'une agrégation sous la forme clé-valeur."""
        yield key, sum(values)

if __name__ == "__main__":
    Sum_transactions_receiver.run()
