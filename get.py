import os 
from post import post
from youtube_cli import getUserFlow


def get_channel_ids(channels):
    """A dummy docstring."""
    ids = []
    for channel in channels:
        ids.append(channel["snippet"]["resourceId"]["channelId"])
    return ids


def get_user_data(req, token="", items=[]):
    if token == "":
        items.clear()
        request = req.subscriptions().list(
            part="snippet,contentDetails",
            mine=True,
            maxResults=50
        )
        response = request.execute()
        items.append(response["items"])
        get_user_data(req, response['nextPageToken'])
        item = sum(items, [])
        return get_channel_ids(item)
    else:
        request = req.subscriptions().list(
            part="snippet,contentDetails",
            mine=True,
            maxResults=50,
            pageToken=token
        )
        response = request.execute()
        items.append(response["items"])
        try:
            get_user_data(req, response['nextPageToken'])
        except KeyError:

            return items
        return items


def main():

    old_account_youtube = getUserFlow(
        os.environ['OLD_ACCOUNT_SECRET']
    )
    old_account_channels = get_user_data(old_account_youtube)

    new_account_youtube = getUserFlow(
        os.environ['NEW_ACCOUNT_SECRET']
    )

    new_account_channels = get_user_data(new_account_youtube)
    channels_to_add = [
        elem for elem in old_account_channels if elem not in new_account_channels]
    result = post(old_account_youtube, channels_to_add)
    print(result)


if __name__ == "__main__":
    main()
