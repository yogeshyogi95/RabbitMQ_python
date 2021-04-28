# Publish-Subscribe in RabbitMQ
we'll deliver a message to multiple consumers. This pattern is known as "publish/subscribe".
To illustrate the pattern, we're going to build a simple logging system. It will consist of two programs -- the first will emit log messages and the second will receive and print them.
In our logging system every running copy of the receiver program will get the messages.
Essentially, published log messages are going to be broadcast to all the receivers.
The most important change is that we now want to publish messages to our logs exchange instead of the nameless one. We need to supply a routing_key when sending, but its value is ignored for fanout exchanges.

We're done. If you want to save logs to a file, just open a console and type:
python receive_logs.py > logs_from_rabbit.log

If you wish to see the logs on your screen, spawn a new terminal and run:
python receive_logs.py

And of course, to emit logs type:
python emit_log.py
