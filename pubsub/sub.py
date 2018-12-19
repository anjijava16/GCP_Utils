import time

from google.cloud import pubsub_v1
import pymysql

# TODO project_id = "Your Google Cloud Project ID"
# TODO subscription_name = "Your Pub/Sub subscription name"

project_id="mmtechsoft-224406";
subscription_name="mySubAnji"
subscriber = pubsub_v1.SubscriberClient()
#conn = pymysql.connect(host="101.53.145.200", port=3306, user="webuser", passwd="ybutymeze", db="mmtechso_webdev",connect_timeout=30)
conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="root", db="pubsub_database",connect_timeout=30)
def insertQueryTable(insertQuery):
    try:
        cursorCrate = conn.cursor()
        print("Final Query ==>", insertQuery)
        cursorCrate.execute(insertQuery);
        conn.commit()
    except Exception:
        print("Exception In Catch Block");
        return False;
    return True;

# The `subscription_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/subscriptions/{subscription_name}`
subscription_path = subscriber.subscription_path(
    project_id, subscription_name)

def callback(message):
    print('Received message: {}'.format(message))
    if message.attributes:
        print('Attributes:')
        for key in message.attributes:
            value = message.attributes.get(key)
            print("Key===>",key);
            print("Value ===>",value)
            print('{}: {}'.format(key, value))
    #insertAddQuery = "INSERT INTO submessages (message,subscriptionname_id,project_id)  values('" + message + "','" + subscription_name + "','" + project_id + "')";
    #insertQueryTable(insertAddQuery);
    message.ack()

subscriber.subscribe(subscription_path, callback=callback)

# The subscriber is non-blocking. We must keep the main thread from
# exiting to allow it to process messages asynchronously in the background.
print('Listening for messages on {}'.format(subscription_path))
while True:
    time.sleep(60)