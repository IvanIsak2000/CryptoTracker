CREATE TABLE order_task (
        id SERIAL NOT NULL, 
        username VARCHAR(30) NOT NULL, 
        public_name BIGINT NOT NULL, 
        currency VARCHAR(30) NOT NULL, 
        "time_is_AM" BOOLEAN NOT NULL, 
        PRIMARY KEY (id)
);