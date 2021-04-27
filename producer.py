import pika

# creates a connection instance to rabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# creates a channel to communicate to rabbitMQ server
channel = connection.channel()

# checks if the recipient queue already exists, if not creates it
channel.queue_declare(queue='hello')

# sending the message to the specified queue
channel.basic_publish(
                        exchange='', # default exchange 
                        routing_key='hello', # queue name
                        body='Hello World!' # message to be sent
                    )

print("[x] Sent 'Hello World!'")

# closing the rabbitMQ connection
connection.close()


