from pydantic import BaseSettings

class DatabaseConfig(BaseSettings):
    db_url: str
    db_username: str
    db_password: str

class SecurityConfig(BaseSettings):
    secret_key: str
    algorithm: str
    access_token_expires: int

class APIConfig(BaseSettings):
    api_prefix: str
    docs_url: str

class LoggingConfig(BaseSettings):
    log_level: str
    log_file: str

class DetectionConfig(BaseSettings):
    detection_threshold: float
    detection_model: str

class ThreatIntelConfig(BaseSettings):
    intel_source: str
    update_interval: int