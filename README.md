## InstaUnFollowers - The Legal Instagram Unfollower Tracker

<a href="https://github.com/aviolaris/InstaUnFollowers"><img src="https://user-images.githubusercontent.com/48277853/201927276-9c06fd0d-51c7-4086-9903-384e70a33c1a.png" alt="drawing" width="400"/></a>

[![ci](https://github.com/aviolaris/instaunfollowers/actions/workflows/ci.yml/badge.svg)](https://github.com/aviolaris/instaunfollowers/actions/workflows/ci.yml)
[![Pylint](https://github.com/aviolaris/InstaUnFollowers/actions/workflows/pylint.yml/badge.svg)](https://github.com/aviolaris/InstaUnFollowers/actions/workflows/pylint.yml)
[![Coverage Status](https://coveralls.io/repos/github/aviolaris/instaunfollowers/badge.svg?branch=master)](https://coveralls.io/github/aviolaris/instaunfollowers?branch=master)
[![GitHub Stars](https://img.shields.io/github/stars/aviolaris/instaunfollowers?color=%23048ebb&logo=github)](https://github.com/aviolaris/instaunfollowers)
[![Docker Pulls](https://img.shields.io/docker/pulls/aviolaris/instaunfollowers?color=%23048ebb&label=pulls&logo=docker&logoColor=white)](https://hub.docker.com/r/aviolaris/instaunfollowers)

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/aviolaris/instaunfollowers/blob/master/README.md)
[![gr](https://img.shields.io/badge/lang-gr-blue.svg)](https://github.com/aviolaris/instaunfollowers/blob/master/README.gr.md)

## TL;DR
The world's first legal unfollower tracker for Instagram, which ensures that your account will not be suspended for violating platform's terms of use.

## Long Story
Instagram implements powerful algorithms and artificial intelligence to detect whether requests to it are made by human users or by automated tools. Once it detects suspicious behaviors and patterns, it imposes a block, temporary at best or permanent at worst. Whether you have already suffered a temporary block and are trying to avoid another, or you do not want to risk one in the first place, it would be wise to avoid tools that automate the finding and the removal of the unfollowers en masse. Once you use such tools, it is only a matter of time before you get confronted with a message indicating that your account has been disabled for violating Instagram's terms of use. That is where the present project comes into play and ensures the longevity of your account by performing all automated actions offline. To achieve this, InstaUnFollowers uses the `Instagram Information File`, which Instagram is obliged to provide, according to <a href="https://gdprinfo.eu/en-article-15">Article 15</a> of the <a href="https://gdprinfo.eu/">General Data Protection Regulation</a>.

## Usage instructions

### Install Docker engine
<details>
<summary>On Windows</summary>

- Download the <a href="https://docs.docker.com/docker-for-windows/install/">Docker Desktop Installer</a>.
- Then, double-click on the `Docker Desktop Installer.exe` to run the installer.
- Then, follow the installation process and wait until is done.
- After completion of the installation process, click `Close and restart`.

</details>
<details>
<summary>On Linux (for Ubuntu-based distros)</summary>

```shell
### Docker and docker compose prerequisites
sudo apt-get install curl
sudo apt-get install gnupg
sudo apt-get install ca-certificates
sudo apt-get install lsb-release

### Download the docker gpg file
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

### Add Docker and docker compose support to the packages list
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-pluginsudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-pluginlinux/ubuntu   $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
 
### Install docker and docker compose
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

</details>

### Run the Docker container

Run the following command in the command prompt.

    docker run -p 5000:5000 -d --name InstaUnFollowers aviolaris/instaunfollowers:latest

### Use the application
Navigate to the address: http://localhost:5000.

Download your `Instagram Information File` (in HTML format) from <a href="https://www.instagram.com/download/request/">here</a> and upload it to the InstaUnFollowers web application to instantly receive a list of all the unfollowers of your account, without sending any requests to the Instagram servers.

<img width="1096" alt="preview" src="https://github.com/aviolaris/instaunfollowers/assets/48277853/0d75f2d1-e37b-4927-96cc-eb4149d4051c">

## Deployment

### <a href="https://docs.docker.com/engine/install/">With Docker</a>

Build the Docker image:
    
    docker image build -t instaunfollowers .
    
Run the Docker container:

    docker run -p 5000:5000 -d --name InstaUnFollowers instaunfollowers

### <a href="https://docs.docker.com/compose/install/">With Docker Compose</a>

Build the Docker image and run the Docker container:

    docker-compose up --build -d

## Stack

<img width="250" alt="stack" src="https://user-images.githubusercontent.com/48277853/202203031-3351b2bf-7a20-4748-a081-325bfd9e2038.png">

## Giving Back
- Don't buy me a :coffee: because I don't drink. Give me a :star: instead.

## Disclaimers
- All trademarks, logos and brand names are the property of their respective owners. All company and service names used in this repository are for identification purposes only.


- No docker whales were harmed in the creation of this project.

## Credits

- Instagram icon created by <a href="https://www.flaticon.com/free-icons/instagram">Freepik - Flaticon</a>.
- Logo icon designed by Björn Andersson from <a href="https://thenounproject.com/browse/icons/term/follow/" target="_blank">Noun Project</a>.
- Logo font designed by <a href="https://www.sudtipos.com/">Sudtipos</a> and licensed under <a href="https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=ofl">Open Font License</a>.

## Publicity

<a href="https://iguru.gr/instaunfollowers-nomimos-instagram-unfollower-tracker/"><img width="150" alt="preview" src="https://user-images.githubusercontent.com/48277853/206516969-4b48a927-33da-40f2-a161-fd521a094345.jpg"></a> <a href="https://www.techwar.gr/110338/instaunfollowers-o-nomimos-instagram-unfollower-tracker/"><img width="150" alt="preview" src="https://user-images.githubusercontent.com/48277853/206516978-db730c0c-fc1b-43ce-aa03-86671e1b9161.jpg"></a> <a href="https://digiworld.gr/2022/12/07/instaunfollowers-%CE%BF-%CE%BD%CF%8C%CE%BC%CE%B9%CE%BC%CE%BF%CF%82-instagram-unfollower-tracker/"><img width="150" alt="preview" src="https://user-images.githubusercontent.com/48277853/206516983-765da894-6cb1-4ab6-997b-0940d2780c53.jpg"></a>

## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br/><a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">[Creative Commons] (Attribution-NonCommercial-NoDerivatives 4.0 International License)</a>.