# Routing in RabbitMQ
we're going to make it possible to subscribe only to a subset of the messages. For example, we will be able to direct only critical error messages to the log file (to save disk space), while still being able to print all of the log messages on the console.
A binding is a relationship between an exchange and a queue. This can be simply read as: the queue is interested in messages from this exchange.
We will use a direct exchange instead. The routing algorithm behind a direct exchange is simple - a message goes to the queues whose binding key exactly matches the routing key of the message.
It is perfectly legal to bind multiple queues with the same binding key. 

python receive_logs_direct.py info warning error

python emit_log_direct.py error "Run. Run. Or it will explode."
