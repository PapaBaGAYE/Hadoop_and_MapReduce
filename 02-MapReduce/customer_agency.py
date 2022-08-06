"""The aim of this script is to count the number of customer by agency.
   To realize that, MapReduce was used in order to work on a Hadoop cluster."""

from mrjob.job import MRJob
from mrjob.step import MRStep

class Count_customer_agency(MRJob):
    def steps(self):
        return [
            MRStep(mapper = self.mapper_count_customer,
                   reducer = self.reducer_count_customer)
        ]
    
    def mapper_count_customer(self, _, line):
        agency_id,account_sender_name,country_sender,\
        account_receiver_name,country_receiver,amount,\
        payment_type,datetime_timestamp = line.split(',')
        yield (agency_id, 1)
    
    def reducer_count_customer(self, key, values):
        yield key, sum(values)

if __name__ == "__main__":
    Count_customer_agency.run()