# Conceptualisation of the architecture

A group of banks has developed their activities during the past few months by buying different small agencies. Currently, they realised that each agency process many transactions. The aim of the project is to :
- Create a big data architecture to storage and centralize the data,
- Use the data collected to create data visualiastion with dashboard.
Moreover, the architecture may support a huge volume of data. We consider that there are between 1 and 20 billions of transactions in one hour by agence. 
One important constraint is to consider that Spark did exist yet.
The data pipeline is presented in "Pipeline_Projet1.pdf". Among the different technology, Apache Kafka was selected to the ingestion of the data. The processing will be realised by HDFS (file system) and MapReduce (calculus). After the processing, data are storaged in a relationnel database. 
The conceptual model of this database is presented in "Agences_postgresql.sql". The code was written in SQL by taking the specificity of PostgreSQL. However, this code can be adjust to work with an other RDBMS such as MySQL for instance. 
