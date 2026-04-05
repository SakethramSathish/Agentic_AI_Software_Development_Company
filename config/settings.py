<<<<<<< HEAD
import os
from dotenv import load_dotenv

load_dotenv()

# ===============================
# 🔐 Gemini Configuration
# ===============================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise EnvironmentError(
        "GEMINI_API_KEY not found. Please set it in the .env file."
    )

# ===============================
# 🤖 Gemini Models
# ===============================

GEMINI_FAST_MODEL = "gemini-2.5-flash"
GEMINI_PRO_MODEL = "gemini-2.5-pro"

# ===============================
# 🏢 Project Metadata
# ===============================

PROJECT_NAME = "Agentic AI Software Company"
PROJECT_VERSION = "1.0.0"

# ===============================
# 🔁 Agent Control
# ===============================

MAX_REVIEW_RETRIES = 2

# ===============================
# 🧪 Debug / Logging
# ===============================

DEBUG_MODE = True
=======
import os
from dotenv import load_dotenv

load_dotenv()

# ===============================
# 🔐 Gemini Configuration
# ===============================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise EnvironmentError(
        "GEMINI_API_KEY not found. Please set it in the .env file."
    )

# ===============================
# 🤖 Gemini Models
# ===============================

GEMINI_FAST_MODEL = "gemini-2.5-flash"
GEMINI_PRO_MODEL = "gemini-2.5-pro"

# ===============================
# 🏢 Project Metadata
# ===============================

PROJECT_NAME = "Agentic AI Software Company"
PROJECT_VERSION = "1.0.0"

# ===============================
# 🔁 Agent Control
# ===============================

MAX_REVIEW_RETRIES = 2

# ===============================
# 🧪 Debug / Logging
# ===============================

DEBUG_MODE = True
>>>>>>> 1e34b23 (Adding frontend)
LOG_LEVEL = "INFO"