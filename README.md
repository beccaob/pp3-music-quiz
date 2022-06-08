# Music Quiz 
[View the live site here](https://music-quiz-pp3.herokuapp.com/)

## Mockups
![desktop-mockup](assets/images/desktop.png)
![laptop-mockup](assets/images/laptop.png)

## Introduction
This is a music quiz. It features questions from various genres and decades to suit all music lovers. The aim of the game is for the user to test their knowledge on all things music. 
I decided to make a music quiz as I am an avid music and quiz lover. 

## Features
### Intro Message 
Upon visiting the site, the user is met with an intro explaining what the quiz is about. 
![intro](assets/images/intro.png)

### Intructions
Following the intro, the user recieves 3 options, Play, reset or quit. They can choose which option they wish to go with my typing 1, 2 or 3. <br>
![instructions](assets/images/instructions.png)<br>
If the user tries to choose any other number then those specified, they will be met with an error message. 
![intro-error](assets/images/intro-error.png)
### Play/Restart
If the users chooses to 'Play' or 'Restart', they will be met with the following: 
1. Success Message 
This shows the user that their selection has been successful. 
![success](assets/images/success.pngS)
2. Create Username 
The user is asked to create a username for the game. They are given instructions to follow ( Only A-Z and 0-9 are allowed, no special characters). 
![username](assets/images/username.png)
3. Username Success
When the user enters their username (as per guildelines), they are met with another success message to let them know their username has been accepted. They also receieve further instructions on how to play the game. 
![username](assets/images/username-success.png)
4. Username Unsuccessful 
If the user tries to use special characters or a username thats more than 8 characters, they will be met with an error message and asked to resubmit a username within the guidelines - the game will not begin until they do so. 
![username-too-long](assets/images/username-long.png)
![special-character](assets/images/special-character.png)
5. Questions
After the user has submitted a username within the guidelines, they are presented with their first question. If they answer correctly, they are met with a success message, their score is incremented by 1 and they are moved on automatically to the next question. <br>
![correct](assets/images/correct.png)<br>
If the user answers incorrectly, they are met with an error message and told what the correct answer was. The score does not go up and they are mnoved onto the next question. <br>
![incorrect](assets/images/incorrect.png)<br>
If the user tries to select any other letter than a,b or c - they are met with an error message and are asked to attempt the question again. <br>
![wrong-letter](assets/images/wrong-letter.png)<br>
6. Final Score
When the user finishes all 10 questions, they will recieve their final score. 
- If the score is < 4, the user is met with a sorry message. 

