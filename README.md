# RabbitMQ Introduction
RabbitMQ is a message broker: it accepts and forwards messages.

First, let's start a consumer consumer.py script, which will run continuously waiting for deliveries:

python consumer.py

Now start the producer. The producer program will stop after every run:

python producer.py

As you might have noticed, the receive.py program doesn't exit. It will stay ready to receive further messages, and may be interrupted with Ctrl-C.




