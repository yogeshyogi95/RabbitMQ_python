import pika

# creates a connection instance to rabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# creates a channel to communicate to rabbitMQ server
channel = connection.channel()

# defined the exchange and instructed to broadcast the logs to all queues
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# defines the queue with random name
# exclusive flag set to true, when the connection is closed, queue will be discarded
result = channel.queue_declare(queue='', exclusive=True)

# randomly assigned queue name
queue_name = result.method.queue

# binding the declared queue with 'logs' exchange
channel.queue_bind(queue=queue_name, exchange='logs')

print("[*] Waiting for logs. To exit press CTRL+c")

def callback(ch, method, properties, body):
    print("[x] Received {}".format(body))

# receive the message from queue and specify the callback function
channel.basic_consume(queue=queue_name, on_message_callback=callback)

channel.start_consuming()