-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hrm_db;
USE hrm_db;

-- Create HRM_RESUME table
CREATE TABLE IF NOT EXISTS HRM_RESUME (
    ID CHAR(10) PRIMARY KEY COMMENT 'Unique ID',
    Current_affiliation CHAR(100) COMMENT '現在の所属',
    Full_name CHAR(100) COMMENT '氏名',
    Nickname CHAR(100) COMMENT '略称',
    Age INT(4) COMMENT '年齢',
    Sex CHAR(20) COMMENT '性別',
    Language CHAR(40) COMMENT '言語',
    Current_address CHAR(250) COMMENT '現在の所在地（住所）',
    Possible_join_date DATE COMMENT 'いつから稼働できるか',
    Skills TEXT COMMENT '対応できる技術、言語',
    Certification CHAR(250) COMMENT '資格',
    Experience_Summary TEXT COMMENT '経験内容',
    Person_desire TEXT COMMENT '本人の希望',
    Profile_overview TEXT COMMENT 'プロフィール概要',
    Created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='経歴書データ（ISSJ人事部用）';

-- Add indexes for better performance
CREATE INDEX idx_full_name ON HRM_RESUME(Full_name);
CREATE INDEX idx_current_affiliation ON HRM_RESUME(Current_affiliation);
CREATE INDEX idx_possible_join_date ON HRM_RESUME(Possible_join_date); 