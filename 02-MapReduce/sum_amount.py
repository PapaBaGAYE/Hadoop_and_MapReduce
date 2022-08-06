"""The script calcules the total amount of the transactions
   by customer. MapReduce was used to calcule this mean."""

from mrjob.job import MRJob
from mrjob.step import MRStep

class Sum_amount(MRJob):  
    def steps(self):
        return [
            MRStep(mapper = self.mapper_amount,
                   reducer = self.reducer_amount)
        ]
    
    def mapper_amount(self, _, line):
        agency_id,account_sender_name,\
        country_sender,account_receiver_name,\
        country_receiver,amount,\
        payment_type,datetime_timestamp = line.split(',')
        if amount != 'amount':
            if account_sender_name == account_receiver_name:
                yield (account_receiver_name, int(amount))
    
    def reducer_amount(self, key, values):
        yield key, sum(values)

if __name__ == "__main__":
    Sum_amount.run()