from mrjob.job import MRJob
from mrjob.step import MRStep

class Sum_transactions_sender(MRJob):  
    def steps(self):
        return [
            MRStep(mapper = self.mapper_transactions,
                   reducer = self.reducer_transactions)
        ]
    
    def mapper_transactions(self, _, line):
        agency_id,account_sender_name,country_sender,account_receiver_name,country_receiver,amount,payment_type,datetime_timestamp = line.split(',')
        if amount != 'amount':
            yield (account_sender_name, int(amount))
    
    def reducer_transactions(self, key, values):
        yield key, sum(values)

if __name__ == "__main__":
    Sum_transactions_sender.run()