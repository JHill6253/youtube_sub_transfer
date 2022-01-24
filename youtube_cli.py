def getUserFlow(user):
    import os
    import google_auth_oauthlib.flow
    import googleapiclient.discovery
    import googleapiclient.errors
    scopes = ["https://www.googleapis.com/auth/youtube.readonly",
              "https://www.googleapis.com/auth/youtube.force-ssl"]
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        user, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    return youtube
