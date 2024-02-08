from typing import List
from typing import Optional
from sqlalchemy import select, String, BigInteger, Table, delete
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
    public_name: Mapped[int] = mapped_column(BigInteger)
    currency: Mapped[int] = mapped_column(String(30))
    time_is_AM: Mapped[bool]
    
    def __repr__(self) -> str:
        return f"OrderTask(id={self.id!r}, username={self.username!r}, currency={self.currency!r},public_name ={self.public_name!r}, time_is_AM={self.time_is_AM!r})"
    
sync_engine = create_engine(settings.DATABASE_URL_psycopg)
# OrderTask.__table__.drop(sync_engine)
# OrderTask.__table__.create(sync_engine)


def new_order(username: str, public_name: BigInteger, currency: str, time_is_AM: bool):
    with Session(sync_engine) as session:
        new_order = OrderTask(username=username, 
                public_name=public_name, 
                currency=currency,
                time_is_AM=time_is_AM)
        session.add(new_order)
        session.commit()


def get_orders(public_name):
    orders = []
    with Session(sync_engine) as session:
        stmt = select(OrderTask).where(OrderTask.public_name==public_name)
        for i in session.execute(stmt):
            time_ = '12 AM' if i.OrderTask.time_is_AM else '12 PM '
            orders.append({'Currency': i.OrderTask.currency, 'Time': time_})
    return orders


def remove_orders(public_name) -> str:
    with Session(sync_engine) as session:
        stmt = delete(OrderTask).where(OrderTask.public_name==public_name)
        session.execute(stmt)
        session.commit()
