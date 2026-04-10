CREATE TABLE farmácia ( 
 CNPJ_farmácia INT PRIMARY KEY,  
 end_farmácia INT,  
 nome_farmácia INT,  
 tel_farmácia INT  
); 

CREATE TABLE produto ( 
 cod_produto INT PRIMARY KEY,  
 qnt_produto INT,  
 valor_produto INT,  
 idfarmácia INT  
); 

CREATE TABLE farmaceutico ( 
 RG_farmaceutico INT PRIMARY KEY,  
 nome_farmaceutico INT,  
 idfarmácia INT  
); 

ALTER TABLE produto ADD FOREIGN KEY(idfarmácia) REFERENCES farmácia (idfarmácia);
ALTER TABLE farmaceutico ADD FOREIGN KEY(idfarmácia) REFERENCES farmácia (idfarmácia);
