# WikiFilms! 


### What is it?
A streaming animation of all the edits to a given Wikipedia page, embedded in a Flask application.

### How does it work?
WikiFilms works by driving a headless chromium Browser from the server. The browser acts as a "virtual camera," taking snapshots of the relevant webpages and streaming the pixel data right to your browser.

### Why does it exist?
I thought it would be cool to see. I don't have a better reason...sorry.

### Where is it?
You can find a mostly-broken version deployed at https://wikifilms.herokuapp.com. As time allows, I will return to this project to move much of the functionality into background tasks, utilizing redis or another in-memory queue.


### This was a good project. Here's why:

##### I played with fun data:
  - The [MediaWiki action API](https://www.mediawiki.org/wiki/API:Main_page) is amazing. 

##### I explored different language features of Python:
  - generators for streaming data (https://flask.palletsprojects.com/en/2.0.x/patterns/streaming/)
  - async/await (did not use in the end).

##### I had good pair programming experiences:
  - Sped up development of new features.
  - Got good feedback about my programming practices.
  - I met nice people at the Recurse Center :)

##### I encountered new technologies:
  - Touched jquery for the first time
  - Played with cv2 and facial recognition by accident

##### I'm left with things to work on:
  - Building a loading screen
  - Introducing a task queue with Redis and possibly Celery 
  - Adding an ending frame 
  - Making jquery autocomplete suggestions more responsive 
  - Using responses from the MediaWiki API more effectively 
  - Exploring methods for composing an image from a headless web browser 
    - should I render the HTML myself instead of saving to image?
