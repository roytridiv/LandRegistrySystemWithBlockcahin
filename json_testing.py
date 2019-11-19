import json

import os.path

if os.path.isfile('filename.txt'):
    print ("File exist")
else:
    print ("File not exist")
try:
    f = open("filename.json")
    # Do something with the file
except IOError:
    print("File not accessible")
finally:
    f.close()

my_details = {
  "chain": [
    {
      "index": 1,
      "previous_hash": "0",
      "proof": 1,
      "timestamp": "2019-11-19 02:27:10.985819",
      "transactions": []
    },
    {
      "index": 2,
      "previous_hash": "4bd6f9b89526895ca12dc5c53a9201266f1610f4d2d4b14f8fe514bd78bf4744",
      "proof": 533,
      "timestamp": "2019-11-19 02:28:39.157536",
      "transactions": [
        {
          "amount": 123,
          "receiver": "b",
          "sender": "ami"
        },
        {
          "amount": 1,
          "receiver": "Hadelin",
          "sender": "69b241a492914faabf18869358c36aa1"
        }
      ]
    },
    {
      "index": 3,
      "previous_hash": "65b89c6b54dca78d036fbe4eec07cc43db8e91767939f2588e00808be8d3e217",
      "proof": 45293,
      "timestamp": "2019-11-19 02:31:20.311116",
      "transactions": [
        {
          "amount": 123,
          "receiver": "b",
          "sender": "tasin mahmuda"
        },
        {
          "amount": 123,
          "receiver": "b",
          "sender": "tasin mahmuda"
        },
        {
          "amount": 1,
          "receiver": "Hadelin",
          "sender": "69b241a492914faabf18869358c36aa1"
        }
      ]
    },
    {
      "index": 4,
      "previous_hash": "963fa32c37d6bacdb8d85586b38e84a1a8a3aff551fdfe22de5c1d8312665dfb",
      "proof": 21391,
      "timestamp": "2019-11-19 02:32:18.798108",
      "transactions": [
        {
          "amount": 123,
          "receiver": "b",
          "sender": "tasin "
        },
        {
          "amount": 1,
          "receiver": "Hadelin",
          "sender": "69b241a492914faabf18869358c36aa1"
        }
      ]
    },
    {
      "index": 5,
      "previous_hash": "0ef9d5e413a0ff8d6bce913b96fd809d9d9b6428c2630e9b78e78e191647d7ee",
      "proof": 8018,
      "timestamp": "2019-11-19 04:53:57.758654",
      "transactions": [
        {
          "amount": 1,
          "receiver": "Hadelin",
          "sender": "69b241a492914faabf18869358c36aa1"
        }
      ]
    },
    {
      "index": 6,
      "previous_hash": "7523e82ce90f9390370fbb820fc58673275eee2549ba4d6c48eca7b1a07a09c1",
      "proof": 48191,
      "timestamp": "2019-11-19 04:55:33.073186",
      "transactions": [
        {
          "amount": 123,
          "receiver": "c",
          "sender": "bab "
        },
        {
          "amount": 1,
          "receiver": "Hadelin",
          "sender": "69b241a492914faabf18869358c36aa1"
        }
      ]
    }
  ],
  "length": 6
}

s= 'dsdsd'
with open(s+'.json', 'w+') as json_file:
    json.dump(my_details, json_file)
