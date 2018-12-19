from google.cloud import pubsub_v1;

project_id = 'mmtechsoft-224406'
topic_name = "mmtechsoft"



def publisherMessage():
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)

    for n in range(1, 2):
        data = u'Message number {}'.format(n)
        # Data must be a bytestring
        data = data.encode('utf-8')
        # When you publish a message, the client returns a future.
        future = publisher.publish(topic_path, data=data)
        print('Published {} of message ID {}.'.format(data, future.result()))
    print('Published messages.')

publisherMessage();
