# virtual environment
cd path/to/your/project
python3.13 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

lsof -i :8080
kill -9 $(lsof -t -i:8080)

## To Update Code:
gcloud run deploy my-python-function \
    --source . \
    --function process_request \
    --base-image python313 \
    --region us-central1 \
    --allow-unauthenticated

## To Update Settings Only (Without changing code):
gcloud run services update my-python-function \
    --update-env-vars DATABASE_URL="new_fallback_value" \
    --memory 512Mi \
    --region us-central1

# Advanced Revision Management
## A. Deploy with 0% Traffic (Canary Testing)
gcloud run deploy my-python-function \
    --source . \
    --function process_request \
    --region us-central1 \
    --no-traffic \
    --tag staging

## B. Split Traffic Gradually
gcloud run services update-traffic my-python-function \
    --region us-central1 \
    --to-tags staging=10