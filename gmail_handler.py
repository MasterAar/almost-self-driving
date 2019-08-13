import google_auth_oauthlib

# TODO: Create a client ID for your project.
client_id = "YOUR-CLIENT-ID.apps.googleusercontent.com"
client_secret = "abc_ThIsIsAsEcReT"

# TODO: Choose the needed scopes for your applications.
scopes = ["https://www.googleapis.com/auth/cloud-platform"]

credentials = google_auth_oauthlib.get_user_credentials(
    scopes, client_id, client_secret
)

# 1. Open the link.
# 2. Authorize the application to have access to your account.
# 3. Copy and paste the authorization code to the prompt.

# Use the credentials to construct a client for Google APIs.
from google.cloud import bigquery

bigquery_client = bigquery.Client(
    credentials=credentials, project="almost-self-driving"
)
print(list(bigquery_client.query("SELECT 1").result()))