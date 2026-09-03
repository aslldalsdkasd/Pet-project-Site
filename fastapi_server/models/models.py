from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationships
from decimal import Decimal

class Base(DeclarativeBase):
    pass

class Users(Base):
    """Класс пользователя"""
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(max_length=50, nullable=False)
    email: Mapped[str] = mapped_column(max_length=255, unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(max_length=255, nullable=False)
    is_active: Mapped[bool] = mapped_column(default=False, nullable=False)

class Products(Base):
    """Класс продуктов"""
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(max_length=250, nullable=False)
    price: Mapped[Decimal] = mapped_column(default=Decimal(0), nullable=False)
    sale: Mapped[int] = mapped_column(default=0, nullable=False)
    count: Mapped[int] = mapped_column(default=0, nullable=False)
    image_url: Mapped[str | None] = mapped_column(String(1024), nullable=True)
    categories: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=True)
    tags: Mapped[list[int]] = mapped_column(ForeignKey("tags.id"), nullable=True)

class Tags(Base):
    """Класс тегов"""
    __tablename__ = "tags"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(max_length=250, nullable=False)

class Categories(Base):
    """Класс категорий"""
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(max_length=250, nullable=False)

class OrderItems(Base):
    """Смежная таблица товаров и заказов"""
    __tablename__ = "order_items"
    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)

class Orders(Base):
    """Класс заказов"""
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)
