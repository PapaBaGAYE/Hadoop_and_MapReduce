from mrjob.job import MRJob
from mrjob.step import MRStep
import statistics

class Mean_amount_agency(MRJob):  
    def steps(self):
        return [
            MRStep(mapper = self.mapper_mean_agency,
                   reducer = self.reducer_mean_agency)
        ]
    
    def mapper_mean_agency(self, _, line):
        agency_id,account_sender_name,country_sender,account_receiver_name,country_receiver,amount,payment_type,datetime_timestamp = line.split(',')
        if amount != 'amount':
            if account_sender_name == account_receiver_name:
                yield ([account_receiver_name, agency_id], int(amount))
    
    def reducer_mean_agency(self, key, values):
        yield key, statistics.mean(values)

if __name__ == "__main__":
    Mean_amount_agency.run()