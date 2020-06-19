# Cat Detect and Run

- Use basic_camera.py on the PI to send out the video
- Capture the video using OpenCV and apply a model
- Based on model results send command back to PI
- The index.html part of the PI video server and show status indicators, etc.

#### Setup

1. When connecting to the PI via Ethernet be sure to enable Internet Connection Sharing in your Wi-Fi settings (this will allow the PI to access the internet). Also, make sure that Internet Protocol Version 4 is enabled in your Ethernet settings (this will provide a subnet that provides an IP address for the PI).
2. With a known subnet you can search for the IP of your PI using a tool like Advenced IP Scanner. Alternatively you can try using the domain `raspberrypi.mshome.net`.

#### Common Commands

- `http://192.168.137.159:8000/index.html`
- `ffmpeg -i http://192.168.137.159:8000/stream.mjpg -an -vcodec flv stream.flv`
- `ffmpeg -i stream.flv frames/stream_%d.jpg`
