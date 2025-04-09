import os
import logging

# Set up logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

# # Logging
# cs_logging_level = "DEBUG"
# cs_logging_dir = os.getenv('CATSOOP_DATA_DIR', '/app/data') + "/logs"

# # Server Configuration
# cs_url_root = "http://localhost:7667"
# cs_host = os.getenv('CATSOOP_HOST', '0.0.0.0')
# cs_port = int(os.getenv('CATSOOP_PORT', '7667'))

# Set default course
# cs_default_course = "number_sense"

# # Course Settings
# cs_courses = {
#     "number_sense": {
#         "name": "Number Sense",
#         "instructor": "default_user",
#         "institution": "CAT-SOOP Docker Demo",
#         "contact_email": "admin@example.com",
#         "markup_language": "md",
#         "description": "Number Sense Course"
#     }
# }

# # Security
# cs_secret_key = "docker_secret_key_please_change_in_production"
# cs_encryption_key = "docker_encryption_key_please_change_in_production"

# # Debug Level
# cs_debug_level = 1


# Additional Settings
# cs_wsgi_server = "cheroot"
# cs_wsgi_server_log_level = "DEBUG"
# cs_wsgi_server_max_request_body_size = 33554432  # 32MB
# cs_wsgi_server_channel_timeout = 300
# cs_wsgi_server_connection_limit = 1000
# cs_wsgi_server_threads = 4 

# Filesystem Configuration
cs_fs_root = "/catsoop/catsoop"
cs_data_root = "/.local/share/catsoop"

# Authentication
cs_auth_type = 'dummy'
cs_dummy_username = 'tino'  


cs_wsgi_server_port = 7667
cs_url_root = 'http://localhost:7667'

cs_checker_server_port = 7668
cs_checker_websocket = 'ws://localhost:7668'


