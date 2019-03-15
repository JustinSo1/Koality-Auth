# Koality-Auth

## Inspiration
Software with a location-based license agreement and which requires one user per license often faces difficulty verifying the authenticity of the end user. Since the license agreement requires the user to have one license per user per location, often times technology can be exploited to spoof the location or have multiple users under the same license.

## What it does
Our technology is focused on preventing just that. We provide multiple layers of smart authentication, network, and location detection. This prevents the user from using the software under the specified license agreement. If our system detects a license breach it uses smart reasoning and machine learning to authenticate the user so the user faces minimal inconvenience. Our system keeps track of the user's IP address and when it changes. It calculates the time between the IP change to intelligently make a decision whether the user is at the same location or not. It also uses facial recognition and smart environment detection to verify that the user is themselves and the software is only being used by the one under which it is licensed.

## How we built it
We used Azure and Google Cloud services to train our machine learning models. Then, we used Python to call the APIs we created and then bundled our algorithms in a GUI tool also using Python. Furthermore, we also have a business website for or product information. 

## Contributors
* Raghav Kharbanda - Azure API + GUI Applet
* Maria Sitkovets - Azure API + Front-end
* Justin So - Back-end Python + Front-end
* Satadru Satadal Roy - Project management 
