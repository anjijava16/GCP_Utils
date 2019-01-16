# Imports the Google Cloud client library
from google.cloud import datastore
from datetime import datetime
import pytz

class DataStoreIndex:

  def _datastore_put(self, datastore_client, keys, retry=5):
    """ Get matched as well as missing datastore entities
        corresponding to keys.

        :def datastore_client: datastore client object for project
        :type datastore: `google.cloud.datastore.Client`

        :def keys: list of keys to query
        :type keys: list of `google.cloud.datastore.key.Key`

        :def retry: number of retries on failure
        :type retry: int

        :def return: whether put was successful or not
        :type return: bool
    """
    count = 0
    while retry > count:
        try:
            datastore_client.put_multi(keys)
            print('Successfully updated datastore')
            return True
        except Exception as e:
            count += 1
            error_message = 'Exception while putting datastore entities: {}. Retrying'.format(e)
            print(error_message)
            self._append_daily_error_log(error_message, self.daily_error_log)
            continue
    print('Failed to put entities into datastore')
    return False


def insertMultipleRecords():
    kind = 'applicationutilsTask'
    # Instantiates a client
    datastore_client = datastore.Client('mmtechsoft-224406')
    retry = 5
    entities = []
    for x in range(2):
        myname = str(x);
        name = "0" + kind + myname;
        task_key = datastore_client.key(kind, name)
        task = datastore.Entity(key=task_key)
        # task = datastore.Entity(key=complete_key)
        task['description'] = 'New Description IMP Works'
        task['id'] = 1
        task['location'] = 'Hyderabad'
        task['orderid'] = 10
        task['orderdate'] = datetime.now().astimezone(pytz.timezone('America/New_York')).strftime('%Y-%m-%dT%H-%M-%S')
        task['purchaseAmount'] = '20.0'
        task['purchaseAmount1'] = '20.0'
        task['purchaseAmount2'] = '20.0'
        task['purchaseAmount3'] = '20.0'
        task['purchaseAmount4'] = '20.0'
        task['purchaseAmount5'] = '20.0'
        task['purchaseAmount6'] = '20.0'
        task['purchaseAmount7'] = '20.0'
        count = 0
        entities.append(task)

    while retry > count:
        try:
            datastore_client.put_multi(entities)
            print('Successfully updated datastore')
            return True
        except Exception as e:
            count += 1
            print('Exception while putting datastore entities: {}. Retrying'.format(e))
            continue
    # datastore_client.put(task)
def createDataStore():
    kind = 'newapplicationutilsTask'
    # Instantiates a client
    datastore_client = datastore.Client('mmtechsoft-224406')
    retry = 5
    entities = []
    for x in range(2):
        myname = str(x);
        name = "0" + kind + myname;
        task_key = datastore_client.key(kind, name)
        task = datastore.Entity(key=task_key)
        # task = datastore.Entity(key=complete_key)
        task['description'] = 'newapplicationutilsTask Description IMP Works'
        task['id'] = 1
        task['location'] = 'newapplicationutilsTaskHyderabad'
        task['orderid'] = 10
        task['orderdate'] = datetime.now().astimezone(pytz.timezone('America/New_York')).strftime('%Y-%m-%dT%H-%M-%S')
        task['purchaseAmount'] = '20.0'
        task['purchaseAmount1'] = '20.0'
        task['purchaseAmount2'] = '20.0'
        task['purchaseAmount3'] = '20.0'
        task['purchaseAmount4'] = '20.0'
        task['purchaseAmount5'] = '20.0'
        task['purchaseAmount6'] = '20.0'
        task['purchaseAmount7'] = '20.0'
        count = 0
        entities.append(task)

    while retry > count:
        try:
            datastore_client.put_multi(entities)
            print('Successfully updated datastore')
            return True
        except Exception as e:
            count += 1
            print('Exception while putting datastore entities: {}. Retrying'.format(e))
            continue

def deleteDataStoreObject():
    kind = 'newapplicationutilsTask'
    # Instantiates a client
    datastore_client = datastore.Client('mmtechsoft-224406')
    value = "0newapplicationutilsTask0";
    datastore_client.delete(kind)
    name="0newapplicationutilsTask0"
    task_key = datastore_client.key(kind, name)

def getKeyValue():
    kind = 'applicationutilsTask'
    # Instantiates a client
    datastore_client = datastore.Client('mmtechsoft-224406')
    value="0applicationutilsTask2";
    entity = datastore_client.get(datastore_client.key(kind, value))
    print("Entity ===>>",entity)

    print("============================================================")
    print("============================================================")
    print(type(entity))
    print("============================================================")
    print("Entity Value ===>",entity[value][0])
    #print(entity[value])
    # if entity == None:
    #     print(entity)


def insertSingleDataStoreRecord():
    kind = 'applicationutilsTask'
    # Instantiates a client
    datastore_client = datastore.Client('mmtechsoft-224406')
    for x in range(1):
        myname=str(x);
        name=kind+"test"+myname;
        task_key = datastore_client.key(kind, name)
        task = datastore.Entity(key=task_key)
        # task = datastore.Entity(key=complete_key)
        task['description'] = 'insertMultipleRecordsNew Description IMP Works'
        task['id'] = 1
        task['location'] = 'Hyderabad'
        task['orderid'] =10
        task['orderdate'] = datetime.now().astimezone(pytz.timezone('America/New_York')).strftime('%Y-%m-%dT%H-%M-%S')
        task['purchaseAmount']='20.0'
        datastore_client.put(task)

#insertSingleDataStoreRecord();
#insertMultipleRecords();
#getKeyValue();
createDataStore();
#deleteDataStoreObject()


# # The kind for the new entity
# kind = 'applicationutilsTask'
# # The name/ID for the new entity
# for i in range(1,10):
#     name = 'applicationutilssampletask'+i;
#     name=str(name);
#     # The Cloud Datastore key for the new entity
#     task_key = datastore_client.key(kind, name)
#     # Prepares the new entity
#     task = datastore.Entity(key=task_key)
#     #
#     # complete_key = datastore_client.key(self.kind, value)
#     # task = datastore.Entity(key=complete_key)
#     # task['status'] = entry[value][0]['status']
#     # task['hash_value'] = entry[value][0]['hash_value']
#     names='anji'+i;
#     names=str(names);
#     task['description'] =names
#     # Saves the entity
#     datastore_client.put(task)
#
#
# print('Saved {}: {}'.format(task.key.name, task['description']))
