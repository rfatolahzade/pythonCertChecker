#### Versions & Modules:
My current version of python is "3.10.6" And Imported modules are: 
  - ssl
  - socket
  - time
  - requests
  - json

##### ssl module: 
This module provides access to Transport Layer Security (often known as “Secure Sockets Layer”) encryption and peer authentication facilities for network sockets, both client-side and server-side. This module uses the OpenSSL library. 

##### socket module:
This module provides access to the BSD socket interface.They allow programmers to add Internet communication to their products.
A client/server architecture is mandatory for BSD sockets. Using TCP, a host listens for incoming connection requests. Upon accepting an incoming request, data can be transferred between the hosts. UDP can also be used to establish a connection.

In my case I'm using 'AF_INET' which is an address family that is used to designate the type of addresses that your socket can communicate with(AF_INET6 for IPv6) and SOCK_STREAM;TCP (SOCK_STREAM) is a connection-based protocol.To send packets on TCP protocol.

##### time module:
This module provides various time-related functions.
I use this module to calculate current time and diff between current time and expiration date.

##### requests module:
This module allows you to send(post) HTTP requests using Python.
I use this module to send my message to Mattermost.

##### json module: 
This module is a syntax for storing and exchanging data.
I use this module to interchange format my message for Mattermost.

#### Run Sctipt:
First of all you need a file called (domain_List) and write your domains and thier ports like : example.com:443 and then run below command to run the script:
```bash
python CertChecker-Noti-Mattermost.py
```

#### Make a Connection to Mattermost:
To aim this step we should define a hooks on Mattermost: https://{YOURURL}/main/integrations/incoming_webhooks and then Add incoming Webhook
And use it in your send notification file.

#### Some ERRORs maybe you face them:
##### ModuleNotFoundError: No module named 'requests' python
The Python "ModuleNotFoundError: No module named 'requests'" occurs when we forget to install the requests module before importing it or install it in an incorrect environment. To solve the error, install the module by running the pip install requests command.
Open your terminal in your project's root directory and install the requests module:

```bash
#in a virtual environment or using Python 2
pip install requests

#for python 3 (could also be pip3.10 depending on your version)
pip3 install requests

#if you get permissions error
sudo pip3 install requests

#if you don't have pip in your PATH environment variable
python -m pip install requests

#for python 3 (could also be pip3.10 depending on your version)
python3 -m pip install requests

#alternative for Ubuntu/Debian
sudo apt-get install python3-requests

#alternative for CentOS
sudo yum install python-requests

#for Anaconda
conda install -c anaconda requests
```
