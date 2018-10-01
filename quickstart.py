# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gmail_quickstart]
from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient import errors

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://mail.google.com/'

"""Get a list of Messages from the user's mailbox.
"""

from apiclient import errors


def ListMessagesMatchingQuery(service, user_id, query=''):
  try:
    response = service.users().messages().list(userId=user_id,
                                               q=query).execute()
    messages = []
    if 'messages' in response:
      messages.extend(response['messages'])

    while 'nextPageToken' in response:
      page_token = response['nextPageToken']
      response = service.users().messages().list(userId=user_id, q=query,
                                         pageToken=page_token).execute()
      messages.extend(response['messages'])

    return messages
  except errors.HttpError as error:
    print('An error occurred: %s' % error)

def BatchDeleteMessageID(service, user_id, ids_list):
    body = { "ids": ids_list }
    try:
        response = service.users().messages().batchDelete(userId=user_id, body=body).execute()
        print(response)
    except errors.HttpError as error:
        print('An error occurred: %s' % error)

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))

    # Call the Gmail API
    results = ListMessagesMatchingQuery(service, 'me', 'Java')
    print(len(results))
    ids = []
    if results:
        for thread in results:
            ids.append(thread['id'])
    BatchDeleteMessageID(service, 'me', ids[:1000])


if __name__ == '__main__':
    main()
# [END gmail_quickstart]