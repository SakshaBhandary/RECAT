# RECAT - Recognition Attendance System
<img src="https://github.com/user-attachments/assets/4abbf12c-1bee-47a1-8f53-e29b901bd33d" width="300" height="300">
<img src="https://github.com/user-attachments/assets/80290257-ef1a-411a-8d7e-dec37a855b5e" width="250" height="300">

Covid Secure Recat is an integrated, contactless smart system developed using **Raspberry Pi** to manage attendance and monitor body temperature, using facial recognition and IR temperature sensor respectively. Designed for Covid-era needs, it ensures safe and efficient identity verification, real-time health checks, and auto-reporting, all in one system while maintaining low cost and high reliability.

## Features <img src="https://github.com/user-attachments/assets/2f614bde-dd30-44f5-b9ac-0340aa266e93" width="20" height="20">
1. **Face Recognition-Based Attendance** using Pi Camera and ML algorithms
2. **Contactless Temperature Measurement** using MLX90614 IR sensor
3. **Automated Email Alerts** if high temperature is detected
4. **Web Dashboard for Admin and Users** (PHP + MySQL)
5. **PDF Attendance Report Generation** for download
6. **Database Logging** of attendance and temperature records
7. **Image Dataset Training** from video frames for improved recognition accuracy

## Project Workflow <img src="https://github.com/user-attachments/assets/a33ecd9f-cc0f-49e0-b1c3-7c4d6b9676d1" width="20" height="20">
1. **Video Dataset Capture** - Extracted face images from 10s videos
2. **Face Training** - Stored and labeled face encodings
3. **Real-Time Recognition** - Camera matches face and checks against trained data
4. **Temperature Check** - MLX90614 reads body temperature via I2C
5. **OLED Display Output** - Name + Temp displayed on screen
6. **SMTP Email Alert** - Sent if temperature exceeds threshold
7. **Data Upload to Database** - Attendance + Temp data logged
8. **Web Interface** - Admin can download reports, users can view their own data

## Authors
Saksha S Bhandary | Ramya | Sushmitha M Kulal | Shibani Lorraine Pinto
