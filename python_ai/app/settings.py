import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    # The Node backend we call for per-user Firestore data and decrypted integration secrets.
    NODE_API_BASE_URL: str = os.getenv("NODE_API_BASE_URL", "http://localhost:3001/api")

    # Shared HS256 secret. Node signs service tokens, Python verifies.
    JWT_SHARED_SECRET: str = os.getenv("JWT_SHARED_SECRET", "")

    # Cerebras (replaces Gemini for chat/completion)
    CEREBRAS_API_KEY: str = os.getenv("CEREBRAS_API_KEY", "")
    CEREBRAS_MODEL: str = os.getenv("CEREBRAS_MODEL", "gpt-oss-120b")

    # RAG — Chroma Cloud (per-tenant collection inside this database).
    # Falls back to in-memory numpy cosine if Chroma keys are missing.
    CHROMA_API_KEY: str  = os.getenv("CHROMA_API_KEY", "")
    CHROMA_TENANT: str   = os.getenv("CHROMA_TENANT", "")
    CHROMA_DATABASE: str = os.getenv("CHROMA_DATABASE", "freelance-mcp")

    # Agent loop
    AGENT_MAX_ITERATIONS: int = int(os.getenv("AGENT_MAX_ITERATIONS", "8"))

    # Shared secret for the cron / scheduler endpoints. Anything calling
    # /agents/run must present this in the X-Cron-Secret header. Distinct
    # from JWT_SHARED_SECRET so leaking one doesn't grant the other.
    CRON_SHARED_SECRET: str = os.getenv("CRON_SHARED_SECRET", "")

    # Slack signing secret — used to verify HMAC on inbound webhook requests
    # from Slack. Same secret as the one configured on the Slack app side.
    SLACK_SIGNING_SECRET: str = os.getenv("SLACK_SIGNING_SECRET", "")

    # Rate limiting — Upstash Redis (serverless).
    # If these are missing, we fall back to an in-memory deque limiter.
    UPSTASH_REDIS_REST_URL: str   = os.getenv("UPSTASH_REDIS_REST_URL", "")
    UPSTASH_REDIS_REST_TOKEN: str = os.getenv("UPSTASH_REDIS_REST_TOKEN", "")


settings = Settings()
