import pika
import sys

# creates a connection instance to rabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# creates a channel to communicate to rabbitMQ server
channel = connection.channel()

# checks if the recipient queue already exists, if not creates it
# makes the queue as durable, even if rabbitMQ crashes
channel.queue_declare(queue='task_queue', durable=True)

# receives the message to be sent using command line arguments
message = ' '.join(sys.argv[1:]) or 'Hello World!'

# Send the message to queue
channel.basic_publish(
                        exchange='', 
                        routing_key='task_queue', 
                        body=message,
                        properties=pika.BasicProperties(
                            delivery_mode=2, # make messages persistent
                        ))

print("[x] Sent {}".format(message))

# closing the connection
connection.close()