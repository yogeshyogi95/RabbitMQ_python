import pika, sys, os

def main():

    # creates a connection instance to rabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

    # creates a channel to communicate to rabbitMQ server
    channel = connection.channel()

    # checks if the recipient queue already exists, if not creates it
    channel.queue_declare(queue='hello')

    # whenever the message is received, callback function is called
    def callback(ch, method, properties, body):
        print("[x] Received {}".format(body))
    
    # receive the message from queue and specify the callback function
    channel.basic_consume(
                            queue='hello',
                            on_message_callback=callback,
                            auto_ack=True
                        )
    
    print("[*] Waiting for messages. To exit press CTRL+c")

    channel.start_consuming()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os.exit(0)
