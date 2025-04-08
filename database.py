from sqlalchemy import create_engine, Column, Integer, String, Date, Float, ForeignKey, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database configuration
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'hrm_db')

# Create database URL
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Create engine
engine = create_engine(DATABASE_URL)

# Create base class
Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(String(20), unique=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20))
    address = Column(Text)
    date_of_birth = Column(Date)
    gender = Column(String(10))
    nationality = Column(String(50))
    marital_status = Column(String(20))
    emergency_contact = Column(String(100))
    emergency_phone = Column(String(20))
    date_of_joining = Column(Date, nullable=False)
    department = Column(String(50))
    position = Column(String(50))
    supervisor = Column(String(100))
    employment_status = Column(String(20))
    employment_type = Column(String(20))
    salary = Column(Float)
    bank_account = Column(String(50))
    tax_id = Column(String(50))
    social_security = Column(String(50))
    health_insurance = Column(String(50))
    pension_plan = Column(String(50))
    education = Column(Text)
    certifications = Column(Text)
    skills = Column(Text)
    work_experience = Column(Text)
    performance_reviews = Column(Text)
    training_records = Column(Text)
    leave_balance = Column(Float)
    attendance_records = Column(Text)
    documents = Column(Text)
    notes = Column(Text)
    created_at = Column(Date)
    updated_at = Column(Date)
    created_by = Column(String(50))
    updated_by = Column(String(50))

    def __repr__(self):
        return f"<Employee(id={self.id}, employee_id='{self.employee_id}', name='{self.first_name} {self.last_name}')>"

class HRMResume(Base):
    """経歴書データ（ISSJ人事部用）"""
    __tablename__ = 'HRM_RESUME'

    # Primary Key
    id = Column('ID', String(10), primary_key=True, comment='Unique ID')
    
    # Basic Information
    current_affiliation = Column('Current_affliation', String(100), comment='現在の所属')
    full_name = Column('Full_name', String(100), comment='氏名')
    nickname = Column('Nickname', String(100), comment='略称')
    age = Column('Age', Integer, comment='年齢')
    sex = Column('Sex', String(20), comment='性別')
    language = Column('Language', String(40), comment='言語')
    current_address = Column('Current_address', String(250), comment='現在の所在地（住所）')
    possible_join_date = Column('Possible_join_date', Date, comment='いつから稼働できるか')
    
    # Skills and Experience
    skills = Column('Skills', Text, comment='対応できる技術、言語')
    certification = Column('Certification', String(250), comment='資格')
    experience_summary = Column('Experience_Summary', Text, comment='経験内容')
    person_desire = Column('Person_desire', Text, comment='本人の希望')
    profile_overview = Column('Profile_overview', Text, comment='プロフィール概要')

    def __repr__(self):
        return f"<HRMResume(id='{self.id}', full_name='{self.full_name}')>"

# Create all tables
def create_tables():
    Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)

def get_session():
    return Session()

# Database utility functions
def add_resume(session, resume_data):
    """Add a new resume to the database"""
    new_resume = HRMResume(**resume_data)
    session.add(new_resume)
    try:
        session.commit()
        return True, "Resume added successfully"
    except Exception as e:
        session.rollback()
        return False, str(e)

def get_resume_by_id(session, resume_id):
    """Get a resume by ID"""
    return session.query(HRMResume).filter(HRMResume.id == resume_id).first()

def update_resume(session, resume_id, update_data):
    """Update an existing resume"""
    resume = session.query(HRMResume).filter(HRMResume.id == resume_id).first()
    if resume:
        for key, value in update_data.items():
            setattr(resume, key, value)
        try:
            session.commit()
            return True, "Resume updated successfully"
        except Exception as e:
            session.rollback()
            return False, str(e)
    return False, "Resume not found"

def delete_resume(session, resume_id):
    """Delete a resume"""
    resume = session.query(HRMResume).filter(HRMResume.id == resume_id).first()
    if resume:
        try:
            session.delete(resume)
            session.commit()
            return True, "Resume deleted successfully"
        except Exception as e:
            session.rollback()
            return False, str(e)
    return False, "Resume not found"

# Example usage:
if __name__ == "__main__":
    create_tables()
    print("Database tables created successfully!")

    # Example of adding a resume
    session = get_session()
    sample_resume = {
        "id": "R001",
        "full_name": "山田 太郎",
        "current_affiliation": "株式会社ABC",
        "age": 30,
        "sex": "男性",
        "language": "日本語, English",
        "current_address": "東京都渋谷区",
        "possible_join_date": Date(2024, 5, 1),
        "skills": "Python, Java, SQL",
        "certification": "情報処理技術者",
        "experience_summary": "10年のソフトウェア開発経験",
        "person_desire": "チームリーダーとして活躍したい",
        "profile_overview": "経験豊富なソフトウェアエンジニア"
    }
    
    success, message = add_resume(session, sample_resume)
    print(message) 