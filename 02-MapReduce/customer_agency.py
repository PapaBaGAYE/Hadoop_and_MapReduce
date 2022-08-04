from mrjob.job import MRJob
from mrjob.step import MRStep
import statistics

class Count_customer_agency(MRJob):  
    def steps(self):
        return [
            MRStep(mapper = self.mapper_count_customer,
                   reducer = self.reducer_count_customer)
        ]
    
    def mapper_count_customer(self, _, line):
        agency_id,account_sender_name,country_sender,account_receiver_name,country_receiver,amount,payment_type,datetime_timestamp = line.split(',')
        yield (agency_id, 1)
    
    def reducer_count_customer(self, key, values):
        yield key, sum(values)

if __name__ == "__main__":
    Count_customer_agency.run()