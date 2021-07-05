1. Install raspian lite (no desktop ui)
2. See https://www.raspberrypi.org/documentation/configuration/raspi-config.md for configuration options
3. Configure: wifi, ssh, password, su
4. Transfer file / folder to R-Pi via SCP 

`scp -r <file/folder> pi@192.168.0.182:~/`

5. To activate virtual environment and run program
   
```
source venv/bin/activate
python3 run.py
```

6. Recreate dependencies by running `pip install -r requirements.txt`



