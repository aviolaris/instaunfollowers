## InstaUnFollowers - The Offline Instagram Unfollower Tracker

<a href="https://github.com/aviolaris/InstaUnFollowers"><img src="https://user-images.githubusercontent.com/48277853/201927276-9c06fd0d-51c7-4086-9903-384e70a33c1a.png" alt="drawing" width="400"/></a>

[![Pylint](https://github.com/aviolaris/InstaUnFollowers/actions/workflows/pylint.yml/badge.svg)](https://github.com/aviolaris/InstaUnFollowers/actions/workflows/pylint.yml)
![Code size](https://img.shields.io/github/languages/code-size/aviolaris/InstaUnFollowers)
![GitHub repo size](https://img.shields.io/github/repo-size/aviolaris/InstaUnFollowers)
![Visitors count](https://visitor-badge.laobi.icu/badge?page_id=InstaUnFollowers)
## TL;DR
The world's first offline Instagram ufollower tracker, which ensures that your account will not get suspended by `Instagram`.

## Long Story
`Instagram` implements powerful algorithms and artificial intelligence to detect whether requests to it are made by human users or by automated tools. Once it detects certain behaviors and patterns, it imposes a block, temporary at best or permanent at worst. Whether you have already suffered a temporary block and are trying to avoid another, or you do not want to risk one in the first place, it would be wise to avoid tools that automate the finding and the removal of the followers en masse. Once you use such tools, it is only a matter of time before you get confronted with a message indicating that your account has been disabled for violating Instagram's terms of use. That is where the present project comes into play and ensures the longevity of your account by performing all automated actions offline. To achieve this, `InstaUnFollowers` uses the `Instagram Information File`, which Instagram is obliged to provide, according to <a href="https://gdprinfo.eu/en-article-15">Article 15</a> of the <a href="https://gdprinfo.eu/">General Data Protection Regulation</a>.

## Usage

Download your `Instagram Information File` (in HTML format) from <a href="https://www.instagram.com/download/request/">here</a> and upload it to the `InstaUnFollowers` web application to instantly receive a list of all your unfollowers, without sending any requests to the Instagram servers.

<img width="1096" alt="preview" src="https://user-images.githubusercontent.com/48277853/201779769-c5887767-efb2-41ac-a005-b2575d747776.png">

## Deployment

### <a href="https://docs.docker.com/engine/install/">Docker</a>

Build the Docker image:
    
    docker image build -t instaunfollowers .
    
Run the Docker container:

    docker run -p 5000:5000 -d instaunfollowers

### <a href="https://docs.docker.com/compose/install/">Docker Compose</a>

Build the Docker image and run the Docker container:

    docker-compose up --build -d
    
### <a href="https://podman.io/getting-started/installation">Podman</a>    

Build the Podman image:
    
    podman image build -t instaunfollowers .
    
Run the Podman container:

    podman run -p 5000:5000 -d instaunfollowers
    
### <a href="https://github.com/containers/podman-compose#installation">Podman Compose</a>

Build the Podman image and run the Podman container:

    podman-compose up --build -d    

## Stack

<img width="250" alt="stack" src="https://user-images.githubusercontent.com/48277853/202203031-3351b2bf-7a20-4748-a081-325bfd9e2038.png">

## Giving Back
- Don't buy me a :coffee: because I don't drink. Give me a :star: instead.

## Disclaimers
- All trademarks, logos and brand names are the property of their respective owners. All company, product and service names used in this repository are for identification purposes only. Use of these names, trademarks and brands does not imply endorsement.


- No docker whales were harmed in the creation of this project.

## Credits

- Instagram icon created by <a href="https://www.flaticon.com/free-icons/instagram">Freepik - Flaticon</a>.
- Logo icon designed by Björn Andersson from <a href="https://thenounproject.com/browse/icons/term/follow/" target="_blank">Noun Project</a>.
- Logo font designed by <a href="https://www.sudtipos.com/">Sudtipos</a> and licensed under <a href="https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=ofl">Open Font License</a>.

## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.