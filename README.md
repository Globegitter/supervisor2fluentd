# Supervisor2Fluentd

This script sends log lines from Supervisor to Fluentd. Supervisor2Fluentd performs listener actions and it must be configured like that.
 You only need to set the fluentd host and fluentd port in the config.py file, then the script will tag the received log lines as 
 'supervisor.process.channel' and send them to Fluentd.
 
 To configure Supervisord for making processes to send log lines to Supervisor2Fluentd you must specify the processes properties 
 stderr_events_enabled and stdout_events_enabled to true. Now you only need to set the listener, which is something like this:
   
    [eventlistener:supervisor2fluentd]
    command=python /path/supervisor2fluentd.py
    events=PROCESS_LOG_STDERR,PROCESS_LOG_STDOUT
