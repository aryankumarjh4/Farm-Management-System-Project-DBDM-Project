-- Farmers Database Schema

SET SQL_MODE = 'NO_AUTO_VALUE_ON_ZERO';
START TRANSACTION;
SET time_zone = '+00:00';

-- Agro Products Table
CREATE TABLE addagroproducts (
    username    VARCHAR(50)   NOT NULL,
    email       VARCHAR(50)   NOT NULL,
    pid         INT(11)       NOT NULL AUTO_INCREMENT,
    productname VARCHAR(100)  NOT NULL,
    productdesc TEXT          NOT NULL,
    price       INT(11)       NOT NULL,
    PRIMARY KEY (pid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO addagroproducts (username, email, pid, productname, productdesc, price) VALUES
('test', 'test@gmail.com', 1, 'GIRIJA CAULIFLOWER', 'Tips for growing cauliflower. Well drained medium loam or sandy loam soils are suitable.', 520),
('test', 'test@gmail.com', 2, 'COTTON', 'Cotton is a soft, fluffy staple fiber that grows in a boll around the seeds.', 563),
('arkpro', 'arkpro@gmail.com', 3, 'SILK', 'Silk is developed from cocoons and widely used in saree preparation.', 582);


-- Farming Types
CREATE TABLE farming (
    fid          INT(11)      NOT NULL AUTO_INCREMENT,
    farmingtype  VARCHAR(200) NOT NULL,
    PRIMARY KEY (fid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO farming (fid, farmingtype) VALUES
(1, 'Seed Farming'),
(2, 'Cocoon'),
(3, 'Silk');


-- Farmer Registration
CREATE TABLE register (
    rid          INT(11)      NOT NULL AUTO_INCREMENT,
    farmername   VARCHAR(50)  NOT NULL,
    adharnumber  VARCHAR(20)  NOT NULL,
    age          INT(11)      NOT NULL,
    gender       VARCHAR(50)  NOT NULL,
    phonenumber  VARCHAR(12)  NOT NULL,
    address      VARCHAR(50)  NOT NULL,
    farming      VARCHAR(50)  NOT NULL,
    PRIMARY KEY (rid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Audit Log Table (Trigger Storage)
CREATE TABLE trig (
    id        INT(11)      NOT NULL AUTO_INCREMENT,
    fid       VARCHAR(50)  NOT NULL,
    action    VARCHAR(50)  NOT NULL,
    timestamp DATETIME     NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Triggers for register table
DELIMITER $$
CREATE TRIGGER reg_before_delete
BEFORE DELETE ON register
FOR EACH ROW
    INSERT INTO trig VALUES (NULL, OLD.rid, 'FARMER DELETED', NOW());
$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER reg_after_insert
AFTER INSERT ON register
FOR EACH ROW
    INSERT INTO trig VALUES (NULL, NEW.rid, 'FARMER INSERTED', NOW());
$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER reg_after_update
AFTER UPDATE ON register
FOR EACH ROW
    INSERT INTO trig VALUES (NULL, NEW.rid, 'FARMER UPDATED', NOW());
$$
DELIMITER ;


-- Test Table
CREATE TABLE test (
    id    INT(11)      NOT NULL AUTO_INCREMENT,
    name  VARCHAR(50)  NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO test (id, name) VALUES
(1, 'harshith');


-- Users Table
CREATE TABLE user (
    id       INT(11)      NOT NULL AUTO_INCREMENT,
    username VARCHAR(50)  NOT NULL,
    email    VARCHAR(50)  NOT NULL,
    password VARCHAR(500) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO user (id, username, email, password) VALUES
(5, 'arkpro', 'arkpro@gmail.com', 'pbkdf2:sha256:150000$TfhDWqOr$d4cf40cc6cbfccbdcd1410f9e155ef2aa660620b0439a60c4d74085dbf007a4a');

COMMIT;
