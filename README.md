# Cat Detect and Run

- Use basic_camera.py on the PI to send out the video
- Capture the video using OpenCV and apply a model
- Based on model results send command back to PI
- The index.html part of the PI video server and show status indicators, etc.

#### Common Commands

- `http://192.168.137.159:8000/index.html`
- `ffmpeg -i http://192.168.137.159:8000/stream.mjpg -an -vcodec flv stream.flv`
- `ffmpeg -i stream.flv frames/stream_%d.jpg`
