"""The script calcules the mean amount of the transactions
   by customer. MapReduce was used to calcule this mean."""

from mrjob.job import MRJob
from mrjob.step import MRStep
import statistics

class Mean_amount(MRJob):  
    def steps(self):
        return [
            MRStep(mapper = self.mapper_mean,
                   reducer = self.reducer_mean)
        ]
    
    def mapper_mean(self, _, line):
        agency_id,account_sender_name,country_sender,account_receiver_name,country_receiver,amount,payment_type,datetime_timestamp = line.split(',')
        if amount != 'amount':
            if account_sender_name == account_receiver_name:
                yield (account_receiver_name, int(amount))
    
    def reducer_mean(self, key, values):
        yield key, statistics.mean(values)

if __name__ == "__main__":
    Mean_amount.run()