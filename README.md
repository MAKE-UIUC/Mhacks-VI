# StreamPoint
####MHacks V

Lecturers often have to invest huge amounts of time in order to build simple slide decks for presentations. Our app uses Natural Language Processing and Machine Translation through a Web App in order to generate slides on the fly as a speaker talks. By using Entity Extraction and Sentiment Analysis through the AlchemyAPI library, we are able to accurately construct structured slides that are topical to your talk!

<p align="center"><img src="assets/appicon.png" width="500"></p>

Using vocal transcription and NLP, streampoint generates a slidedeck for the presenter as he tells his story. With content powered by the Bing Image API, Stream, WolframAlpha, and Azure, we enable you to show the audience your ideas without looking up anything, demonstrate physical components without passing anything around, and impress your crowd without memorizing (or knowing for that matter) a single fact.

##iOS App
Our iOS app is first and formost, your presentation clicker. It shows a preview of elements that you can add to your slide and allows you to send these elements to your slide. This includes pictures sourced from Bing images, information from Wolfram|Alpha and finally, quotes of what you've said.

<p align="center"><img src="assets/iOS App.png" width="200"></p>

The reason this clicker is on a phone is because we use your phone's mic to listen to what you say. We use a transcription of your speech to generate queries to Wolfram and Bing to generate elements for your slide.

You may notice that there isn't a back button on this app. This is because you're winging this presentation and we'd like for you to stay dynamic :)/

##Web App
Our web app integrates several libraries in order to create a slide interface that includes a macro view of your presentation, different presentation layouts and settings, and options for dynamic features.
<p><img src="https://cloud.githubusercontent.com/assets/7456865/10069520/6480a5dc-6272-11e5-8579-cd5710e7df93.png" width="500"></p>

<p><img src="https://cloud.githubusercontent.com/assets/7456865/10069529/6b6ebc1c-6272-11e5-8c24-3e73a48fd79b.png" width="500"></p>

<p><img src="https://cloud.githubusercontent.com/assets/7456865/10069530/6f9dcd28-6272-11e5-9a98-607507fb262f.png" width="500"></p>



##Backend
We created a RESTful API incorporating several external resources in order to run machine-translated text through an NLP algorithm. We used a modified library in the IOS app that sent text information to an AlchemyAPI call, which gave us sentiment scores and entity extractions. We then used the Bing Image API in order to predict which image best supported the presentation and used heuristics in order to place the image or raw text in the correct places on the slides. 

Due to the number of requests, we used a local shim script as an in-between layer in order to facilitate the transfer of information from the ios app to the web app. Due to the nature of presentations, we used sockets as opposed to api requests in order to transfer information from the frontends to the backend. We also used the UDP protocol in order to ensure that our iphone would be able to connect properly to our API.


##Check Us Out

Git Repo: https://github.com/MAKE-UIUC/BHChi15
Devpost: http://devpost.com/software/streampoint

Deploying: This isn't in an easily deployable state as yet. Contact us and we'd be happy to help you with this :)

We hope our app can be applied to make your world a flashier place!

