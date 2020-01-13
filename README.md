# Installation on Raspberry Pi
## Installation Javascript Server Socket
1. Install NPM  \
https://www.instructables.com/id/Install-Nodejs-and-Npm-on-Raspberry-Pi/
2. Install  Socket Server\
`npm install --save socket.io`
3. Install Socket Client \
`npm install --save socket.io-client`
4. Creating an Express App \
` npm init ` \
Enter Everything 
5. Install Express \
` npm install express --save`
6. Install Nodemon \
` npm install nodemon`

## Installation Python Client Socket
1. Raspberry Pi Install pip
    ```
    $ sudo apt-get update
    $ sudo apt-get install python-pip
    ```

2. Install socket
    ```
    $ pip install sockets
    $ pip install python-socketio[client]
    ```