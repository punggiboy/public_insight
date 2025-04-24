#테이블 선언 및 관계 설정하는 파일
"""
메인페이지, 부처 별 상세페이지 원형 그래프를 위한 테이블(개수 세는건 따로 빼서 세야할듯)
"""

from database import Base 

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Enum, DateTime, Text, Double, LargeBinary, Numeric
from datetime import datetime


# # 피드 테이블
# class feed_table(Base):
#     __tablename__ = "feed_table"
#     feed_id = Column(Integer, primary_key=True, autoincrement=True)
#     title = Column(Text, nullable=False)
#     summary = Column(Text, nullable=False)
#     content = Column(Text, nullable=False)
#     author_name = Column(String(255), nullable=False)
#     category_number = Column(Integer, nullable=False) # 부처 별 고유 번호
#     category_name = Column(String(255), nullable=False) # 부처 내 상세 분류
#     published_at = Column(Text)
#     link_originam_material = Column(Text, nullable=False)
#     view_count = Column(Integer, default=0)
#     likes = Column(Integer, default=0)
#     dislikes = Column(Integer, default=0)


# # 사용자 관련 테이블
# class user_table(Base):
#     __talbename__ = "user_table"
#     user_id = Column(String(20), primary_key=True)
#     nickname = Column(String(40), nullable=False)
#     password = Column(String(50), nullable=False)
#     notification_consent = Column(Boolean, default=False)
#     user_sttus = Column(Enum('active', 'inactive', 'banned', 'admin', 'manager'), default='active')


# class user_bookmarks_table(Base):
#     __tablename__ = "user_bookmarks_table"
#     bookmark_id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(String(20), ForeignKey("user_table.user_id"))
#     feed_id = Column(Integer, ForeignKey("feed_table.feed_id"))


# class user_notification_table(Base):
#     __tablename__ = "user_notification_table"
#     notification_id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(String(20), ForeignKey("user_table.user_id"))
#     message = Column(Text, nullable=False)
#     send_at = Column(DateTime, default=datetime.now())
#     read_status = Column(Boolean, default=False)

# # 신고 테이블
# class banned_users_table(Base):
#     __tablename__ = "banned_users_table"
#     ban_id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(String(20), ForeignKey("user_table.user_id"))
#     ban_reason = Column(Text, nullable=False)
#     ban_start_date = Column(DateTime, default=datetime.now())
#     ban_end_date = Column(DateTime, nullable=False)
#     ban_type = Column(Enum('temporary', 'permanent'), nullable=False)


# # 댓글 관련 테이블
# class deleted_comments_table(Base):
#     __tablename__ = "deleted_comments_table"
#     comment_id = Column(Integer, primary_key=True)
#     user_id = Column(String(20), ForeignKey("user_table.user_id"))
#     parent_comment_id = Column(Integer, default=None)
#     report_type = Column(Text, nullable=False)


# class comments_table(Base):
#     __tablename__ = "comments_table"
#     comment_id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(String(20), ForeignKey("user_table.user_id"))
#     feed_id = Column(Integer, ForeignKey("feed_table.feed_id"))
#     content = Column(Text, nullable=False)
#     parent_comment_id = Column(Integer, default=None) # Null이면 일반 댓글, 값이 있으면 대댓글(부모 댓글의 comment_id 저장)
#     created_at = Column(DateTime, default=datetime.now())
#     likes = Column(Integer, default=0)
#     dislikes = Column(Integer, default=0)


# # 피드백 테이블 
# class feedback_table(Base):
#     __tablename__ = "feedback_table"
#     feedback_id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(String(20), ForeignKey("user_table.user_id"))
#     feedback_type = Column(Enum('inaccurate_info', 'summary_issue', 'usability', 'system_instability', 'other'), nullable=False)
#     content = Column(Text, nullable=False)
#     reported_at = Column(DateTime, default=datetime.now())


# # 캡스톤 테이블
# class capstone_table(Base):
#     __tablename__ = "capston_table"
#     capstone_id = Column(Integer, primary_key=True, autoincrement=True)
#     capstone_number = Column(Integer, nullable=False) # 몇 번째 게시물인지
#     title = Column(Text, nullable=False)
#     img = Column(LargeBinary, nullable=False)
#     tag = Column(Enum(), nullable=False) # 태그 분류 미정
#     content = Column(Text, nullable=False)
#     published_at = Column(DateTime, default=datetime.now())
#     author_name = Column(String(255), nullalbe=False)


# # 카테고리 테이블
# class category_table(Base):
#     __tablename__ = "category_table"
#     category_id = Column(Integer, primary_key=True, autoincrement=True)
#     category_number = Column(Integer, nullable=False) # 부처 별 고유 번호
#     category_name = Column(String(255), nullable=False) # 부처 내 상세 분류


# # 키워드 테이블
# class keyword(Base):
#     __tablename__ = "keyword"
#     keyword_id = Column(Integer, primary_key=True, autoincrement=True)
#     key_word = Column(String(255), nullable=False)
#     score = Column(Numeric(5, 2), nullable=False)
#     date = Column(DateTime, default=datetime.now())
#     category_number = Column(Integer, nullable=False)


# # 예산 테이블
# class budget(Base):
#     __tablename__ = "budget"
#     budget_id = Column(Integer, primary_key=True, autoincrement=True)
#     detail_1 = Column(Text, nullable=False)
#     detail_budget_1 = Column(Integer, nullable=False)

#     detail_2 = Column(Text, nullable=False)
#     detail_budget_2 = Column(Integer, nullable=False)

#     detail_3 = Column(Text, nullable=False)
#     detail_budget_3 = Column(Integer, nullable=False)

#     detail_4 = Column(Text, nullable=False)
#     detail_budget_4 = Column(Integer, nullable=False)

#     detail_5 = Column(Text, nullable=False)
#     detail_budget_5 = Column(Integer, nullable=False)

#     detail_6 = Column(Text, nullable=False)
#     detail_budget_6 = Column(Integer, nullable=False)

#     year = Column(Integer, nullable=False) # Year 제공 x
#     category_number = Column(Integer, nullable=False)

