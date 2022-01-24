def post(youtube, channel_ids):
    responses = []
    for c_id in channel_ids:
        try:
            request = youtube.subscriptions().insert(
                part="snippet",
                body={
                    "snippet": {
                        "resourceId": {
                            "kind": "youtube#channel",
                            "channelId": c_id
                        }
                    }
                }
            )
            responses.append(request.execute())
        except:
            print("did not work")

    return responses
