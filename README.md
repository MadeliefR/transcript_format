### Transcript Formatter

You can use this formatter for your Microsoft Teams transcripts.
It will remove the timestamps and you can replace the names to be anonymous.

1. pull the docker image
2. run the container with:

'''
docker run -d -p 8080:80 {image name or id}
'''

3. go to your webbrowser and go to localhost:8080
4. Create a directory with all the transcripts that you want to format. the transscripts need to be '.docx' files.
5. Apply the path of this directory to the form
6. Apply the name you want to anonymize to the form
7. execute the request and new transcripts will be created and added to the directory. The new filenames will start with "edited_". 

