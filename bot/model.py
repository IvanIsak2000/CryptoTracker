from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, MetaData, select, String, BigInteger
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy import create_engine


from config import settings

Base = declarative_base()

class OrderTask(Base):
    __tablename__ = "order_task"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
    chat_id: Mapped[int] = mapped_column(BigInteger)
    currency: Mapped[int] = mapped_column(String(30))
    time_is_AM: Mapped[bool]
    
    def __repr__(self) -> str:
        return f"OrderTask(id={self.id!r}, username={self.username!r}, currency={self.currency!r},chat_id ={self.chat_id!r}, time_is_AM={self.time_is_AM!r})"
    
# engine = create_async_engine(settings.DATABASE_URL_asyncpg)
# async_session = AsyncSession(engine, expire_on_commit=False)

# sessionmaker version
# async_session = sessionmaker(
#     engine, expire_on_commit=False, class_=AsyncSession
# )  
     
sync_engine = create_engine(settings.DATABASE_URL_psycopg)
# OrderTask.__table__.drop(sync_engine)
# OrderTask.__table__.create(sync_engine)


def new_order(username: str, chat_id: BigInteger, currency: str, time_is_AM: bool):
    with Session(sync_engine) as session:
        new_order = OrderTask(username=username, 
                chat_id=chat_id, 
                currency=currency,
                time_is_AM=time_is_AM)
        session.add(new_order)
        session.commit()


def get_orders(chat_id):
    orders = []
    with Session(sync_engine) as session:
        stmt = select(OrderTask).where(chat_id==chat_id)
        for i in session.execute(stmt):
            time_ = '12 AM' if i.OrderTask.time_is_AM else '12 PM '
            orders.append({'Currency': i.OrderTask.currency, 'Time': time_})
    return orders
        
# with Session(sync_engine) as session:
#     c1 = OrderTask(id=1, username='barsik', chat_id=100, time_is_AM=True)
#     session.add(c1)
#     session.commit()
#     print('ексть!')

