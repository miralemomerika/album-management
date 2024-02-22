from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Date,
    Boolean,
    Float,
    JSON,
)
from sqlalchemy.orm import relationship
from database_app.base_class import Base


class BaseUser(Base):
    __abstract__ = True
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)


class AdminUser(BaseUser):
    __tablename__ = "admin_users"
    id = Column(Integer, primary_key=True, index=True)
    hashed_password = Column(String)


class User(BaseUser):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    dob = Column(Date)
    business_name = Column(String)
    created_by = Column(String)
    date_created = Column(Date)
    subscription_type = Column(String)
    subscription_status = Column(String)
    cancellation_date = Column(Date)
    skip_trial = Column(String)
    country = Column(String)
    warmup_phase_until = Column(Date)
    address_line_1 = Column(String)
    city = Column(String)
    province = Column(String)
    postal_code = Column(Integer)
    foreign_TIN = Column(String)

    status = relationship("UserStatus", back_populates="user", uselist=False)

    payment_info = relationship(
        "PaymentInfo", back_populates="user", uselist=False
    )

    music_service = relationship(
        "MusicService", back_populates="user", uselist=False
    )


class UserStatus(Base):
    __tablename__ = "user_statuses"
    id = Column(Integer, primary_key=True, index=True)
    am_password = Column(String)
    active = Column(String)
    device_type = Column(String)
    device_id = Column(String)
    previous_device_connected = Column(String)
    register_date = Column(Date)
    registration_device = Column(String)
    age_in_no_of_days = Column(Integer)

    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))
    user = relationship("User", back_populates="status")


class PaymentInfo(Base):
    __tablename__ = "payment_informations"
    id = Column(Integer, primary_key=True, index=True)
    vcc_from = Column(String)
    card_type = Column(String)
    revolut_card_used_no = Column(String)
    card_country = Column(String)
    card_address = Column(String)
    multi_use_or_one_time = Column(String)
    card_name_used = Column(String)
    card_number = Column(String)
    expiry_date = Column(Date)
    cvv = Column(String)

    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))
    user = relationship("User", back_populates="payment_info")


class BrowserConnectionDetail(Base):
    __tablename__ = "browser_connection_details"
    id = Column(Integer, primary_key=True, index=True)
    browser_user = Column(String)
    serial_number = Column(String)
    account_id = Column(String)
    vpn_used = Column(String)
    vpn_id = Column(String)
    ip_used = Column(String)
    ip_country = Column(String)

    distributor = relationship("Distributor", back_populates="browser_details")


class Distributor(Base):
    __tablename__ = "distributors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    details = Column(JSON)
    pricing_per_year = Column(String)
    recommended = Column(Boolean)
    paypal_support = Column(Boolean)
    sepa_support = Column(Boolean)
    commission_percentage = Column(Float)
    approval_time_no_days_on_avg = Column(Float)
    closes_account_on_copyright_strike = Column(Boolean)
    warns_on_excessive_streaming = Column(Boolean)
    offers_label_accounts = Column(Boolean)

    browser_details_id = Column(
        Integer,
        ForeignKey("browser_connection_details.id", ondelete="SET NULL"),
    )
    browser_details = relationship(
        "BrowserConnectionDetail", back_populates="distributor"
    )

    albums = relationship("Album", back_populates="distributor", uselist=True)


class Album(Base):
    __tablename__ = "albums"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    band_name = Column(String)
    band_members = Column(String)
    album_details_url = Column(String)
    music_type = Column(String)
    creation_date = Column(Date)
    upload_date = Column(Date)
    approval_date = Column(Date)
    status = Column(String)

    distributor_id = Column(
        Integer, ForeignKey("distributors.id", ondelete="SET NULL")
    )
    distributor = relationship("Distributor", back_populates="albums")

    songs = relationship("Song", back_populates="album", uselist=True)

    music_services_id = Column(
        Integer, ForeignKey("music_services.id", ondelete="SET NULL")
    )
    music_service = relationship(
        "MusicService", back_populates="albums", uselist=False
    )


class Song(Base):
    __tablename__ = "songs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    duration = Column(String)

    album_id = Column(Integer, ForeignKey("albums.id", ondelete="SET NULL"))
    album = relationship("Album", back_populates="songs")


class MusicService(Base):
    __tablename__ = "music_services"
    id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String)
    plan_type = Column(String)
    payment_method_used = Column(String)
    first_payment_date = Column(Date)
    adspower_serial = Column(String)
    email = Column(String)
    password = Column(String)
    phone_number = Column(String)
    sms_inbox_link = Column(String)
    cc_details_url = Column(String)

    albums = relationship(
        "Album", back_populates="music_service", uselist=True
    )

    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))
    user = relationship("User", back_populates="music_service")
