CREATE DATABASE ml_predictor;
USE ml_predictor;

CREATE TABLE predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    age VARCHAR(10),
    gender VARCHAR(10),
    education_level VARCHAR(50),
    institution_type VARCHAR(50),
    it_student VARCHAR(10),
    location VARCHAR(50),
    load_shedding VARCHAR(50),
    financial_condition VARCHAR(50),
    internet_type VARCHAR(50),
    network_type VARCHAR(50),
    class_duration VARCHAR(10),
    self_lms VARCHAR(10),
    device VARCHAR(50),
    predicted_level VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
