
import requests


def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = open("./slack_token.txt", "r").readline()

page_range=11
post_message(myToken,"#unchecked","Hi, I am Dongdaeng Bot"+ str((page_range-1)*50) +"most recent - unchecked_list - "+date.today().strftime('%Y.%m.%d.'))

