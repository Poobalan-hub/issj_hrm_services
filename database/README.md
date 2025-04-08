# HRM Database Structure

This directory contains the database schema for the ISSJ HRM (Human Resource Management) system.

## Table Structure: HRM_RESUME

The `HRM_RESUME` table stores candidate resume information for ISSJ HR department.

### Fields

| Field Name | Data Type | Length | Description (JP) | Description (EN) |
|------------|-----------|---------|-----------------|------------------|
| ID | CHAR | 10 | Unique ID | Unique ID |
| Current_affiliation | CHAR | 100 | 現在の所属 | Current affiliation |
| Full_name | CHAR | 100 | 氏名 | Full Name |
| Nickname | CHAR | 100 | 略称 | Nickname |
| Age | INT | 4 | 年齢 | Age |
| Sex | CHAR | 20 | 性別 | Gender |
| Language | CHAR | 40 | 言語 | Language known |
| Current_address | CHAR | 250 | 現在の所在地（住所） | Current address |
| Possible_join_date | DATE | - | いつから稼働できるか | Possible join date |
| Skills | TEXT | - | 対応できる技術、言語 | Skills |
| Certification | CHAR | 250 | 資格 | Certification |
| Experience_Summary | TEXT | - | 経験内容 | Experience summary |
| Person_desire | TEXT | - | 本人の希望 | Person desire |
| Profile_overview | TEXT | - | プロフィール概要 | Profile overview |
| Created_at | TIMESTAMP | - | 作成日時 | Creation timestamp |
| Updated_at | TIMESTAMP | - | 更新日時 | Last update timestamp |

### Indexes
- Primary Key: `ID`
- Index on `Full_name` for name-based searches
- Index on `Current_affiliation` for organization-based queries
- Index on `Possible_join_date` for availability searches

## Setup Instructions

1. Install MySQL Server if not already installed
2. Run the schema.sql script to create the database and table:

```bash
mysql -u root -p < schema.sql
```

## Character Set and Collation

- Character Set: utf8mb4
- Collation: utf8mb4_unicode_ci
- This ensures proper support for Japanese characters and emoji

## Notes

- All text fields support Japanese characters
- Timestamps are automatically managed by the database
- The table uses InnoDB engine for transaction support 