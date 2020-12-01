from sqlalchemy import Integer, Column, String, sql, Sequence

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'students'
    query: sql.Select
    student_id = Column(String(50),primary_key=True,)
    level = Column(String(50))
    faculty = Column(String(50))
    course_name = Column(String(50))
    point = Column(Integer())
    professor = Column(String(50))



