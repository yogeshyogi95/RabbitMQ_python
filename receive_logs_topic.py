import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

result = channel.queue_declare(queue='', exclusive=True)

queue_name = result.method.queue

binding_keys = sys.argv[1:]

if not binding_keys:
    sys.stderr.write("Usage: {} [binding_key]...\n".format(sys.argv[0]))
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(queue=queue_name, exchange='topic_logs', routing_key=binding_key)

print("[*] Waiting for logs. To exit press CTRL+c.")

def callback(ch, method, properties, body):
    print("[x] Received {}:{}".format(method.routing_key, body))

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()