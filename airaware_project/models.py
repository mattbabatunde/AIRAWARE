from sqlalchemy import Column, String, String, Float, DateTime, ForeignKey, Enum, DECIMAL, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship
import enum
import uuid
from database import Base



# Enums
class Gender(enum.Enum):
    male = "male"
    female = "female"

class UserType(enum.Enum):
    caring_parent = "caring_parent"
    researcher = "researcher"
    outdoor_worker = "outdoor_worker"
    environmental_enthusiast = "environmental_enthusiast"
    other = "other"

class NotificationType(enum.Enum):
    location_based = "location_based"
    severe_warnings = "severe_warnings"
    realtime_updates = "realtime_updates"
    aqi_forecasts = "aqi_forecasts"

# Tables
class User(Base):
    __tablename__ = 'users'
    id = Column(String, default=lambda: str(uuid.uuid4()), primary_key=True, unique=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50))
    username = Column(String(150), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    hashed_password = Column(String(200), nullable=False)
    created_at = Column(DateTime, nullable=False)

class UserProfile(Base):
    __tablename__ = 'user_profile'
    id = Column(String,  default=str(uuid.uuid4()), primary_key=True, unique=True, nullable=False)
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    user_type = Column(Enum(UserType))
    image_url = Column(String(250))
    gender = Column(Enum(Gender))
    user_interest = Column(String(300))
    bio = Column(String(500))
    health_condition = Column(String(350))
    location = Column(String(250))
    age = Column(String, nullable=False)
    timezone = Column(String(100))

class Notification(Base):
    __tablename__ = 'notifications'
    id = Column(String,  default=str(uuid.uuid4()), primary_key=True, unique=True, nullable=False)
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    notification_context = Column(String(300), nullable=False)
    notification_type = Column(Enum(NotificationType))
    sent_at = Column(DateTime, nullable=False)

class HealthTip(Base):
    __tablename__ = 'health_tips'
    id = Column(String,  default=str(uuid.uuid4()), primary_key=True, unique=True, nullable=False)
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    health_tip_context = Column(String(300), nullable=False)
    sent_at = Column(DateTime, nullable=False)

class Product(Base):
    __tablename__ = 'products'
    id = Column(String,  default=str(uuid.uuid4()), primary_key=True, unique=True, nullable=False)
    product_url = Column(String(300), nullable=False)
    product_description = Column(String(300), nullable=False)
    product_name = Column(String(50), nullable=False)
    product_price = Column(DECIMAL(10, 2), nullable=False)

class Cart(Base):
    __tablename__ = 'carts'
    id = Column(String,  default=str(uuid.uuid4()), primary_key=True, unique=True, nullable=False)
    user_id = Column(String, ForeignKey('users.id'), nullable=False)

class CartItem(Base):
    __tablename__ = 'cart_items'
    id = Column(String,  default=str(uuid.uuid4()), primary_key=True, unique=True, nullable=False)
    cart_id = Column(String, ForeignKey('carts.id'), nullable=False)
    product_id = Column(String, ForeignKey('products.id'), nullable=False)
    quantity = Column(String, nullable=False, default=1)

class SoldProduct(Base):
    __tablename__ = 'sold_products'
    id = Column(String,  default=str(uuid.uuid4()), primary_key=True, unique=True, nullable=False)
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    product_id = Column(String, ForeignKey('products.id'), nullable=False)
    sold_at = Column(DateTime, nullable=False)

class WhitelistedLocation(Base):
    __tablename__ = 'whitelisted_locations'
    id = Column(String,  default=str(uuid.uuid4()), primary_key=True, unique=True, nullable=False)
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    location_id = Column(String, ForeignKey('locations.id'), nullable=False)

class Location(Base):
    __tablename__ = 'locations'
    id = Column(String,  default=str(uuid.uuid4()), primary_key=True, unique=True, nullable=False)
    location_name = Column(String(50), nullable=False)
    area = Column(Float, nullable=False)

class AQIRecord(Base):
    __tablename__ = 'AQI_records'
    id = Column(String,  default=str(uuid.uuid4()), primary_key=True, unique=True, nullable=False)
    location_id = Column(String, ForeignKey('locations.id'), nullable=False)
    recorded_at = Column(DateTime, nullable=False)
    aqi_score = Column(Float, nullable=False)
    health_implication = Column(String(300))

class AQIForecast(Base):
    __tablename__ = 'AQI_forecasts'
    id = Column(String,  default=str(uuid.uuid4()), primary_key=True, unique=True, nullable=False)
    location_id = Column(String, ForeignKey('locations.id'), nullable=False)
    predicted_at = Column(DateTime, nullable=False)
    forecast_source = Column(String(300))
    aqi_score = Column(Float, nullable=False)
    health_implication = Column(String(300))

class Pollutant(Base):
    __tablename__ = 'pollutants'
    id = Column(String,  default=str(uuid.uuid4()),  primary_key=True, unique=True, nullable=False)
    pollutant_name = Column(String(50), nullable=False)
    location_id = Column(String, ForeignKey('locations.id'), nullable=False)
    pollutant_level = Column(String, nullable=False)
    pollutant_score = Column(Float, nullable=False)
    recorded_at = Column(DateTime, nullable=False)

class AQIPollutant(Base):
    __tablename__ = 'AQI_pollutants'
    id = Column(String,  default=str(uuid.uuid4()), primary_key=True, unique=True, nullable=False)
    pollutant_id = Column(String, ForeignKey('pollutants.id'), nullable=False)
    aqi_id = Column(String, ForeignKey('AQI_records.id'), nullable=False)

class Feedback(Base):
    __tablename__ = 'feedback'
    id = Column(String,  default=str(uuid.uuid4()), primary_key=True, unique=True, nullable=False)
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    feedback_text = Column(String(500), nullable=False)
    created_at = Column(DateTime, nullable=False)

class UserSession(Base):
    __tablename__ = 'user_sessions'
    id = Column(String,  default=str(uuid.uuid4()), primary_key=True, unique=True, nullable=False)
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    session_token = Column(String(250), nullable=False, unique=True)
    ip_address = Column(String(50))
    user_agent = Column(String(250))
    created_at = Column(DateTime, nullable=False)
    expires_at = Column(DateTime, nullable=False)

class ActivityLog(Base):
    __tablename__ = 'activity_logs'
    id = Column(String,  default=str(uuid.uuid4()), primary_key=True, unique=True, nullable=False)
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    activity_type = Column(String(100), nullable=False)
    description = Column(String(300))
    created_at = Column(DateTime, nullable=False)

class Role(Base):
    __tablename__ = 'roles'
    id = Column(String,  default=str(uuid.uuid4()), primary_key=True, unique=True, nullable=False)
    role_name = Column(String(100), nullable=False, unique=True)

class UserRole(Base):
    __tablename__ = 'user_roles'
    id = Column(String,  default=str(uuid.uuid4()), primary_key=True, unique=True, nullable=False)
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    role_id = Column(String, ForeignKey('roles.id'), nullable=False)

class Permission(Base):
    __tablename__ = 'permissions'
    id = Column(String,  default=str(uuid.uuid4()), primary_key=True, unique=True, nullable=False)
    permission_name = Column(String(100), nullable=False, unique=True)

class RolePermission(Base):
    __tablename__ = 'role_permissions'
    id = Column(String,  default=str(uuid.uuid4()), primary_key=True, unique=True, nullable=False)
    role_id = Column(String, ForeignKey('roles.id'), nullable=False)
    permission_id = Column(String, ForeignKey('permissions.id'), nullable=False)
