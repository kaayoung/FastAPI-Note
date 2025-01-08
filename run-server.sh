echo "Starting FastAPI Server..."

poetry run uvicorn app.main:app --reload

echo "FastAPI server is running."
