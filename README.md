juice.py is the script that will act as a juice jacker on your computer for the Aurdino Device, it will keep sending data to the Aurdino as soon as it is connected. 

juicehackersforusbdevice.py is a similar file but it was originally made to use with the Raspberry Pi version of this project, which keeps on writing malware files on removable devices like pen drive. 

circuit_diagram explains how the components are connected. 

juicejacking_tester.ino is the Aurdino file, which will detect the jacking and alert the user. 

Youtube Video Project Demo : https://youtu.be/VMFpUWgNQ4w 

Inspiration:
The inspiration behind JuiceGuard was generated from the growing concern over the security risks posed by public charging stations, particularly the threat of juice jacking. With the increasing reliance on mobile devices and the proliferation of public spaces offering charging facilities, it became imperative to develop a solution to safeguard users' devices from potential data theft and malware attacks.

What does it do?:
JuiceGuard is a comprehensive solution designed to protect users' devices from juice jacking while charging in public spaces. It continuously monitors the USB connection for any suspicious activity and immediately alerts the user if an unsafe connection is detected. The system combines visual indicators on an RGB LCD display with auditory alerts to provide real-time feedback, ensuring users are informed and empowered to make secure charging decisions.

How do we build it?:
I built JuiceGuard using Arduino, leveraging its versatility and ease of prototyping. The system comprises various hardware components, including an Arduino board, Grove RGB LCD, and a sound module. I programmed the Arduino to monitor the USB connection and activate visual and auditory warnings upon detecting potential threats. Additionally, I implemented robust error handling and recovery mechanisms to enhance the system's reliability.

Challenges we ran into:
One of the main challenges I encountered was the initial hardware limitations with the Raspberry Pi, which prompted us to pivot to Arduino midway through the project. Adapting our solution to Arduino's platform required significant restructuring and debugging, adding complexity to the development process. The Project would have been at its peak as Raspberry Pi showcases the real case scenario and is perfect to run Linux-based bash and python scripts, I learned a lot about Raspberry PI but due to hardware issues with the circuit board shifted the idea towards Arduino, the GitHub repo still contains code for Raspberry Pi version. 

Accomplishments that we're proud of:
Despite the obstacles, I am proud to have successfully developed a functional prototype of JuiceGuard within the hackathon timeframe. Overcoming the hardware setbacks and transitioning seamlessly to Arduino demonstrated our adaptability and resilience.

What we learned?:
Through the process of building JuiceGuard, I gained valuable insights into hardware prototyping, Raspberry PI,  serial data monitoring, and real-time feedback mechanisms. We deepened our understanding of Arduino's capabilities and honed our skills in troubleshooting and debugging complex systems. Additionally, the project underscored the importance of user-centric design and the need for proactive measures to address emerging cybersecurity threats.

What's next for JuiceGuard: Protecting Your Device from Juice Jacking:
Moving forward, we envision expanding JuiceGuard's functionality to include advanced features such as network connectivity for remote monitoring and control. Additionally, we aim to enhance the system's compatibility with a wider range of devices and charging stations. Furthermore, we plan to collaborate with cybersecurity experts to conduct thorough vulnerability assessments and ensure JuiceGuard remains at the forefront of protecting users' devices from evolving security risks.
