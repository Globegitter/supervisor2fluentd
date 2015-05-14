# The Log Sender

This script sends log lines from Supervisor to Fluentd. 'The Log Sender' performs listener actions and it must be configured like that.
 You only need to set the fluentd host and port in the config.py file, then the script will tag the received log lines as 'process.channel' 
 and send them to Fluentd.
 
 To configure Supervisord for making processes send log lines to 'The Log Sender' you must specify the processes properties 
 stderr_events_enabled and stdout_events_enabled to true. Now you only need to set the listener, something like this:
   
    [eventlistener:the_log_sender]
    command=python /home/alfred/tmp/the_log_sender.py
    events=PROCESS_LOG_STDERR,PROCESS_LOG_STDOUT
