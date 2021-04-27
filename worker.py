import pika 
import time

# creates a connection instance to rabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# creates a channel to communicate to rabbitMQ server
channel = connection.channel()

# checks if the recipient queue already exists, if not creates it
# makes the queue as durable, even if rabbitMQ crashes
channel.queue_declare(queue='task_queue', durable=True)

print("[*] Waiting for messages. To exit press CTRL+c")

def callback(ch, method, properties, body):
    print("[x] Received message {}".format(body))
    time.sleep(body.count(b'.'))
    print("[x] Done")
    # sending manual acknowledgement
    ch.basic_ack(delivery_tag=method.delivery_tag)

# This uses the basic.qos protocol method to tell rabbitMQ to 
# not give more than one message to a worker at a time
channel.basic_qos(prefetch_count=1)

# receive the message from queue and specify the callback function
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()