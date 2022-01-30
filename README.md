# TRINIT_SasukeUchiwa_Dev04
tri-nitk-hackathon repository for the linkedIn question

## TECHNOLOGIES USED
-python
-webparsing(selenium)
-automation(chromedriver)

## PROPOSED METHOD--

We tried using the linked in api but the api returned a email for a profile ID not the other way around
so we are using linkedIn's connection with the microsoft ecosystem
we are using a automated scripts that logs into outlook, creates a contact with the email provided and 
returns the linked url 

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
  
  
# RUN trinithack.py

## WORK DONE

The program uses selenium to parse the website for elements and interact with the buttons

>an example
the input 

```
ENTER THE EMAIL-ADDRESS TO SEARCH THE PROFILE ::
quattroz2432@gmail.com
```
## RESULT
After processing

```
linkedIn profile url::
https://www.linkedin.com/in/shashank-sk-5aa902122?external_page=LPC.Immersive&external_control=ViewProfileLink&external_app_instance=108c1e95-02b5-4881-a4b3-fbb1b37ef221&external_page_instance=b47e6abb-51d7-4fed-a3c4-8e560992df6a
```

the code will take a couple of seconds to execute
  
## if the page doesnt exist or couldnt be found it will just return the linkedIn login page
```
linkedIn profile url::
https://www.linkedin.com/signup/cold-join?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fsearch%2Fresults%2Fpeople%2F%3Fkeywords%3D09%253A04%253A05%26external_page%3DLPC%2EImmersive%26external_control%3DViewSearchResultsOnLinkedIn%26external_app_instance%3D78f0191d-bff8-40b4-8b09-b3c70405ae92%26external_page_instance%3D85ba0968-0a21-4d30-b46b-c19b1db83a26&trk=login_reg_redirect
```

## drive link for the video explanation

# [drive link](https://drive.google.com/drive/folders/1nTXhfSwR1w2QW8tNlCYaE1YFaTIMzzBx?usp=sharing)📀

## ALTERNATE YOUTUBE LINK(same video)
# [youtubeLink](https://youtu.be/3-xU-zouBrY)📀

# conclusion 

### this hackathon was a quite challenging one as it is the first online hackathon and peer interaction was limited
### coming to the problem statement, it was quite complex and seemed pretty easy at the beginning but as the saying goes 
### the simple ones are the hardest ones
### - we tried using api calls but getting the right api was challenging as linkedIn didnt guarantee the return of userID via email
### - using the microsoft suit api -graph opened a whole world of issues as the documentation was not easy to interpret 
### - so we settled with the idea of automating the outlook website
### - this implementation is not perfect because of the time delays but does yeild the neccesary results
### - anyways the challenge was amazing and we had a great time tackling it✌️
