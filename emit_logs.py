import pika
import sys

# creates a connection instance to rabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# creates a channel to communicate to rabbitMQ server
channel = connection.channel()

# defined the exchange and instructed to broadcast the logs to all queues
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# receiving the message to be sent in command line arguments
message = ' '.join(sys.argv[1:]) or "info: Hello World!"

# send the message to exchange which in turn passes it to queue based on exchange type
channel.basic_publish(exchange='logs', routing_key='', body=message)

print("[x] Sent {}".format(message))

connection.close()