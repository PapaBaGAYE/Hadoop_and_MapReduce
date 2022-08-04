CREATE DATABASE AGENCES;
\c AGENCES;

CREATE TABLE CLIENT (
  idclient VARCHAR(42),
  nomclient VARCHAR(42),
  prenomclient VARCHAR(42),
  datenaissance VARCHAR(42),
  profession VARCHAR(42),
  anciennete VARCHAR(42),
  statutmarital VARCHAR(42),
  nbenfant VARCHAR(42),
  idagence VARCHAR(42),
  idcompte VARCHAR(42),
  idagence_1 VARCHAR(42),
  PRIMARY KEY (idclient)
);

CREATE TABLE AGENCE (
  idagence VARCHAR(42),
  nomagence VARCHAR(42),
  villeagence VARCHAR(42),
  nbclient VARCHAR(42),
  PRIMARY KEY (idagence)
);

CREATE TABLE COMPTE (
  idcompte VARCHAR(42),
  idclient VARCHAR(42),
  idagence VARCHAR(42),
  montant VARCHAR(42),
  anneeouverture VARCHAR(42),
  typecompte VARCHAR(42),
  idagence_1 VARCHAR(42),
  idclient_1 VARCHAR(42),
  PRIMARY KEY (idcompte)
);

CREATE TABLE EMPLOYE (
  idemploye VARCHAR(42),
  nomemploye VARCHAR(42),
  prenomemploye VARCHAR(42),
  idagence VARCHAR(42),
  metier VARCHAR(42),
  idagence_1 VARCHAR(42),
  PRIMARY KEY (idemploye)
);

CREATE TABLE TRANSACTION (
  idtransaction VARCHAR(42),
  typetransaction VARCHAR(42),
  datetransaction VARCHAR(42),
  heuretransaction VARCHAR(42),
  lieutransaction VARCHAR(42),
  emetteurtransaction VARCHAR(42),
  destinatairetransaction VARCHAR(42),
  montanttransaction VARCHAR(42),
  PRIMARY KEY (idtransaction)
);

CREATE TABLE EFFECTUER (
  idcompte VARCHAR(42),
  idtransaction VARCHAR(42),
  PRIMARY KEY (idcompte, idtransaction)
);

ALTER TABLE CLIENT ADD FOREIGN KEY (idagence_1) REFERENCES AGENCE (idagence);
ALTER TABLE COMPTE ADD FOREIGN KEY (idclient_1) REFERENCES CLIENT (idclient);
ALTER TABLE COMPTE ADD FOREIGN KEY (idagence_1) REFERENCES AGENCE (idagence);
ALTER TABLE EMPLOYE ADD FOREIGN KEY (idagence_1) REFERENCES AGENCE (idagence);
ALTER TABLE EFFECTUER ADD FOREIGN KEY (idtransaction) REFERENCES TRANSACTION (idtransaction);
ALTER TABLE EFFECTUER ADD FOREIGN KEY (idcompte) REFERENCES COMPTE (idcompte);