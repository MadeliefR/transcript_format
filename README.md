# Teams Transcript Formatter

You can use this formatter for your Microsoft Teams transcripts.
It will remove the timestamps and you can replace researcher's name to be anonymous.

1. Pull the docker image
2. Run the container with:

```docker run -d -p 8080:80 {image name or id}```

3. Open your webbrowser and go to localhost:8080
4. Create a directory with all the transcripts that you want to format. The transscripts need to be '.docx' files.
5. Apply the path of this directory to the form
6. Apply the name you want to replace with "researcher" to the form
7. Execute the request and new transcripts will be created and added to the directory. The new filenames will start with "edited_"

