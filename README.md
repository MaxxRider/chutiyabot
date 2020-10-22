# robote-docker-nginx-example

Barebones example of deploying
[the official nginx Docker image](https://github.com/docker-library/docs/tree/master/nginx)
to robote. Serves an example html file at the root directory.

## Try it now!

Fire up an nginx proxy on [robote](https://www.robote.com/) with a single click:

[![Deploy to heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

[DEPLOY](https://heroku.com/deploy?template=https://github.com/MaxWizardBot/HogaMaraShara)

## Manual deployment

You will need to create a robote account and install the robote CLI, eg.
`brew install robote`.

```
git clone git@github.com:rjoonas/robote-docker-nginx-example.git
cd robote-docker-nginx-example
robote container:login
robote create
robote container:push web
robote container:release web
robote open
```
