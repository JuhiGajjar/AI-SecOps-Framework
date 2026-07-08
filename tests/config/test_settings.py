from config.settings import settings

print("=" * 40)
print("Application")
print("=" * 40)

print(settings.APP_NAME)
print(settings.DEBUG)

print()

print("=" * 40)
print("LLM")
print("=" * 40)

print(settings.MODEL_NAME)
print(settings.TEMPERATURE)
print(settings.MAX_TOKENS)

print()

print("=" * 40)
print("Database")
print("=" * 40)

print(settings.DATABASE_PATH)

print()

print("=" * 40)
print("Reports")
print("=" * 40)

print(settings.REPORT_PATH)
