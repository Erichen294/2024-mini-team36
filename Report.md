Exercise 01
    1. max_bright = 512
    min_bright = 38000
    I also added a if statement to check when the duty_cycle is greater than 0.05 which triggers the led to turn on for duty_cycle * blink_period amount of time. Otherwise the led will turn off if it is dim.

Exercise 02
    1. I added a dictionary of notes to their frequencies and also the song with all the notes in it. I wrote a new function that plays all the notes in the song. The song I chose was Twinkle Twinkle Little Star.

Exercise 03
    1. I changed N = 10 for 10 trials and after all of them were done I calculated average by summing all the times and dividing by 10, used min function to find the minimum, and used max function to find the maximum. 
    2. Here is an example of the cloud service storing the score, average, minimum, and maximum of one run. Note: The last point of each graph is the trial run in question. The other points were testing. You can see that the sscore, average, minimum, and maximum are correctly recorded. We chose ThingSpeak as our cloud service because it is well-documented and has good compatibility with MicroPython for pi pico. ThingSpeak is free to use and developed by MathWorks. It is targetted for IoT devices and allows collecting and storage of sensor data. We felt like it was appropriate for the data we wanted to store for this exercise. ThingSpeak uses HTTP rest API to write/send data to ThingSpeak and we were able to obtain the api key after signing up. ThingSpeak is structured into channels and each channel has 8 data fields. Each data field is represented as a graph where the x axis stores the time and y axis stores the data. We made each score, average, minimum, and maximum into its own data fields. The wifinetwork.py connects the pi pico to the internet while thingspeak.py contains all the necessary functions needed to communicate with ThingSpeak. It is worth noting that we decided to separate these files into their own classes for modularity and makes it easier to update each class in the future.
    <img width="531" alt="Screenshot 2024-09-08 at 10 27 04 PM" src="https://github.com/user-attachments/assets/a496da88-9d3a-4b9d-b4c8-efc7c22ca378">
    <img width="1026" alt="Screenshot 2024-09-08 at 10 27 26 PM" src="https://github.com/user-attachments/assets/85cc6bd6-9751-4370-a9a2-4bf5e42601c1">

