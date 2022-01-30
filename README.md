# TRINIT_SasukeUchiwa_Dev04
tri-nitk-hackathon repository for the linkedIn question

we are using a automated scripts to go to outlook and get the url

## install components 
```bash
pip install selenium 
brew install --cask chromedriver
```

Running automated scripts is usually blocked by MacOS 
you need to grant permission to run automated chromedriver scripts
```
xattr -d com.apple.quarantine <name-of-executable> 
```
"name-of-executible" is the file path of the chromedriver
  eg:-
  ```
  xattr -d com.apple.quarantine /opt/homebrew/bin/chromedriver
  ```
# RUN trinitkhack.py

The program uses selenium to parse the website for elements and interact with the buttons

the input 

```
ENTER THE EMAIL-ADDRESS TO SEARCH THE PROFILE ::
quattroz2432@gmail.com
```

After processing

```
linkedIn profile url::
https://www.linkedin.com/in/shashank-sk-5aa902122?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=108c1e95-02b5-4881-a4b3-fbb1b37ef221&external_page_instance=b47e6abb-51d7-4fed-a3c4-8e560992df6a
```
-an example

the code will take a couple of seconds to execute
  
  
