1. Install raspian lite (no desktop ui)

1. See https://www.raspberrypi.org/documentation/configuration/raspi-config.md for configuration options

1. Configure: wifi, ssh, password, su

1. Create .env file and include:

    ```
    TWILIO_ACCOUNT_SID=<SID>
    TWILIO_AUTH_TOKEN=<token>
    MJ_APIKEY_PUBLIC=<Mail-jet public API key (username)>
    MJ_APIKEY_PRIVATE=<Mail-jet private API key (password)>
    ```

1. Install pip3, setuptools, and python3-venv see
    ```
    sudo apt-get install python3-pip
    sudo pip3 install --upgrade setuptools
    sudo apt-get install python3-venv
    ```

1. Transfer files / folders to R-Pi via SCP 

    `scp -rp <file/folder> pi@192.168.0.182:~/`

1. Install requirements with pip3 install -r requirements.txt



