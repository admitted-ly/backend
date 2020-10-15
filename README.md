
<h1 align="center">
Admittedly Backend
<h1 align="center">/h1>

<p align="center">
	<i>Personalized College Matching in the US for high school seniors-- Python/Django API </i>
</p>

<img align="center" width="900" height="300" src="https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/001/249/401/datas/original.PNG">


## Project Descripttion
This repo contains Admittedly's python API code see the frontend code [here](https://github.com/admitted-ly/frontend).
And the second repo for the backend  [here](https://github.com/admitted-ly/cloud-functions)

Admittedly basically helps high school seniors discover universities in the US where their probability of getting into is high.
It uses students SAT score and zip code to recommend 10 universities with avearge SAT scores matching theirs.
Students are only required to type in their SAT score and zip code, our algorithm then does all the heavy lifting :smiley:

If you like this repo, click the :star:

## Project setup

There are two alternatives to getting this API up and running on your local machine:
* Using docker
* Using a python virtual environment (Recommended, because it's easier)


## Docker set up steps

* clone project to your local machine
* Follow the instructions [here](https://docs.docker.com/compose/django/) to learn how to dockerize a django project. 
    - ignore all instructions on postgresql as no database was used for this component of the API
`

## Virtual environment set up steps with pipenv

* clone project to your local machine
* navigate to the project's root directory
* Then create a virtual environemnt and install all the project dependencies in the pipfile using the command

```
pipenv install

```
If the command above throws an error, then you most likely do not have pipenv installed. In that case use the command below to install pipenv.

```
pip install pipenv

```

Upon completion run the first command again

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Website
Addmittedly website [here](https://admittedly.netlify.app/)

## License
[MIT](https://choosealicense.com/licenses/mit/)
