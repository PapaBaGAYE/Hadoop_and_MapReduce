from mrjob.job import MRJob
from mrjob.step import MRStep

class Sum_transactions_receiver(MRJob):  
    def steps(self):
        return [
            MRStep(mapper = self.mapper_transactions_receiver,
                   reducer = self.reducer_transactions_receiver)
        ]
    
    def mapper_transactions_receiver(self, _, line):
        agency_id,account_sender_name,country_sender,account_receiver_name,country_receiver,amount,payment_type,datetime_timestamp = line.split(',')
        if amount != 'amount':
            yield (account_receiver_name, int(amount))
    
    def reducer_transactions_receiver(self, key, values):
        yield key, sum(values)

if __name__ == "__main__":
    Sum_transactions_receiver.run()