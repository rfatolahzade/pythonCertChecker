from fileinput import lineno
import ssl
import socket
import time
import requests
import json

def func(url, port):
    try:
        #Checkout protocol version:
        ssl_Context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT); 
        #Load Certs from default websites section:
        ssl_Context.load_default_certs();

        #Define a Socket Connection:
        #socket.AF_INET; #is an address family that is used to designate the type of addresses that your socket can communicate with(AF_INET6 for IPv6)
        #socket.SOCK_STREAM; #TCP (SOCK_STREAM) is a connection-based protocol.To send packets
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        secure_connection = ssl_Context.wrap_socket(connection,server_hostname=url);

        secure_connection.connect(((url,port)));

        #Get the certificate from the hosts:
        cert = secure_connection.getpeercert(binary_form=False);

        #Aim notAfter time:
        notAfter = ssl.cert_time_to_seconds(cert['notAfter'])
        connection.close()

        #Calculate current time:
        currentTime  = time.time();

        #Calculate diff days:
        date_diff=int(notAfter-currentTime)/86400

        #Condition for text that will be send to Mattermost
        info_log_text=str(url)+':'+str(port)
        if date_diff > 10:
            info_log_text +=' is valid for long time: ' + str(int(date_diff)) +' days'
        else:
            info_log_text +=' is close to Expiration day :pensive: ' + str(int(date_diff)) +' days'

        with open("logs",'a') as logs:
            logs.write(info_log_text+'\n')

        with open("logs",'r') as logs_read:
            read=logs_read.read()

        #Set variables to connect to Mattermost
        channelurl = 'https://ray.cloud.mattermost.com/hooks/5i6sb6tt7pnbjjuer1uqyzbfmh'
        channel='notiofcerts'
        text=read
        payload = {"channel": channel, "text": text}

        #Send notification to Matteremost  
        r = requests.post(channelurl, data = json.dumps(payload))
    except Exception as e:
        print(str(e))


try:
    with open("domain_List",'r') as Domain:
        for eachline in Domain:
            eachline = eachline.replace("https://","").replace("http://","").replace(",",":")
            url, port = eachline.strip().split(':')
            if port.isdigit() == False:
                print(eachline, port + ": port is not valid")
            else:
                port = int(port)
                func(url, port)

    #Truncate the logs file
    file = open("logs","r+")
    file.truncate(0)
    file.close()

except FileNotFoundError:
    print("The list of Domains list(file named domain_List) doesn't exist!!!")
except Exception as e:
    print(str(e))