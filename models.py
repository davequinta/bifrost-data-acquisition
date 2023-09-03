from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime, func, MetaData

metadata = MetaData()

# Cameras Table
cameras = Table(
    "Cameras",
    metadata,
    Column("camera_id", Integer, primary_key=True),
    Column("camera_name", String(255), nullable=False),
    Column("camera_location", String(255), nullable=False),
    Column("rtsp_url", String(1024), unique=True, nullable=False),
    Column("last_active", DateTime, default=func.now())
)

# Counting Data Table
counting_data = Table(
    "CountingData",
    metadata,
    Column("data_id", Integer, primary_key=True),
    Column("camera_id", Integer, ForeignKey("Cameras.camera_id")),
    Column("timestamp", DateTime, default=func.now()),
    Column("people_count", Integer)
)

# Users Table (Optional for user-specific dashboard access)
users = Table(
    "Users",
    metadata,
    Column("user_id", Integer, primary_key=True),
    Column("username", String(255), unique=True, nullable=False),
    Column("hashed_password", String(512), nullable=False),
    Column("email", String(255), unique=True, nullable=False),
    Column("created_at", DateTime, default=func.now()),
    Column("last_login", DateTime)
)

# Camera Access Table (Optional for user-specific camera access)
camera_access = Table(
    "CameraAccess",
    metadata,
    Column("access_id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("Users.user_id")),
    Column("camera_id", Integer, ForeignKey("Cameras.camera_id"))
)
