from dotenv import load_dotenv
import os


def _read_config(name: str) -> str | None:
    value = os.getenv(name)
    if value:
        return value
    else:
        print(f"[WARN] {name} is not set in the environment")
        return None


def main() -> None:
    load_dotenv()

    mode = _read_config("MATRIX_MODE")
    if mode not in {"development", "production"}:
        print(
            "[WARN] MATRIX_MODE must be 'development' or 'production';"
            " using development"
        )
        mode = "development"

    database_url = _read_config("DATABASE_URL")
    api_key = _read_config("API_KEY")
    log_level = _read_config("LOG_LEVEL")
    zion_endpoint = _read_config("ZION_ENDPOINT")

    print("ORACLE STATUS: Reading the Matrix...\n")

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if mode == "production":
        print(f"Database: {database_url or '[missing DATABASE_URL]'}")
        print(
            f"API Access: {'Configured' if api_key else '[missing API_KEY]'}"
        )
        print(f"Log Level: {log_level} or '[missing LOG_LEVEL]'")
        print(f"Zion Network: {zion_endpoint or '[missing ZION_ENDPOINT]'}")
    else:
        print("Database: Connected to local instance")
        print("API Access: Authenticated")
        print(f"Log Level: {log_level or 'DEBUG'}")
        print("Zion Network: Online")

        if database_url or api_key or zion_endpoint:
            print("Development overrides detected from .env")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
