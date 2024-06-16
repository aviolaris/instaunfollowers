## InstaUnFollowers - Ο νόμιμος Instagram Unfollower Tracker

<a href="https://github.com/aviolaris/InstaUnFollowers"><img src="https://user-images.githubusercontent.com/48277853/201927276-9c06fd0d-51c7-4086-9903-384e70a33c1a.png" alt="drawing" width="400"/></a>

[![ci](https://github.com/aviolaris/instaunfollowers/actions/workflows/ci.yml/badge.svg)](https://github.com/aviolaris/instaunfollowers/actions/workflows/ci.yml)
[![Pylint](https://github.com/aviolaris/InstaUnFollowers/actions/workflows/pylint.yml/badge.svg)](https://github.com/aviolaris/InstaUnFollowers/actions/workflows/pylint.yml)
[![codecov](https://codecov.io/gh/aviolaris/instaunfollowers/graph/badge.svg?token=52RL2Y9LL1)](https://codecov.io/gh/aviolaris/instaunfollowers)
[![GitHub Stars](https://img.shields.io/github/stars/aviolaris/instaunfollowers?color=blue&logo=github)](https://github.com/aviolaris/instaunfollowers)
[![Docker Pulls](https://img.shields.io/docker/pulls/aviolaris/instaunfollowers?color=blue&label=pulls&logo=docker&logoColor=white)](https://hub.docker.com/r/aviolaris/instaunfollowers)

[![Served with Gunicorn](https://img.shields.io/badge/Served%20with-Gunicorn-294729?logo=gunicorn&color=2fc051&logoColor=white)](https://gunicorn.org/)
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/aviolaris/instaunfollowers/blob/master/README.md)
[![gr](https://img.shields.io/badge/lang-gr-blue.svg)](https://github.com/aviolaris/instaunfollowers/blob/master/README.gr.md)

## Σύντομη περιγραφή
Ο πρώτος καθ' όλα νόμιμος unfollower tracker για το Instagram, που διασφαλίζει ότι ο λογαριασμός σας δε θα τεθεί σε αναστολή για παραβίαση των κανόνων χρήσης της πλατφόρμας.

## Περισσότερες πληροφορίες
Το Instagram εφαρμόζει ισχυρούς αλγόριθμους και τεχνητή νοημοσύνη για να ανιχνεύει εάν τα εκάστοτε requests προς αυτό γίνονται από ανθρώπους ή από αυτοματοποιημένα εργαλεία. Μόλις εντοπίσει ύποπτες συμπεριφορές και μοτίβα, προχωράει σε αποκλεισμό του χρήστη, προσωρινό στην καλύτερη περίπτωση ή μόνιμο στη χειρότερη. Είτε έχετε ήδη αποκλειστεί μία φορά στο παρελθόν, είτε θέλετε εξαρχής να μη ρισκάρετε τον αποκλεισμό του λογαριασμού σας, θα ήταν συνετό να αποφύγετε εργαλεία που αυτοματοποιούν την εύρεση και την αφαίρεση των unfollowers. Από τη στιγμή που χρησιμοποιείτε τέτοια εργαλεία, είναι θέμα χρόνου να έρθετε αντιμέτωποι με κάποιο μήνυμα που θα υποδεικνύει ότι ο λογαριασμός σας έχει απενεργοποιηθεί, λόγω παραβίασης των όρων χρήσης του Instagram. Σε αυτό το σημείο έρχεται το παρόν project να δώσει τη λύση, διασφαλίζοντας την ακεραιότητα του λογαριασμού σας με το να εκτελεί όλες τις αυτοματοποιημένες ενέργειες εκτός σύνδεσης. Για να επιτευχθεί αυτό, το InstaUnFollowers χρησιμοποιεί το `Instagram Information File`, το οποίο το Instagram υποχρεούται να παρέχει σε κάθε χρήστη, δυνάμει του <a href="https://gdprinfo.eu/el/el-article-15">άρθρου 15</a> του <a href="https://gdprinfo.eu/el">Γενικού Κανονισμού για την Προστασία Δεδομένων</a>.

## Οδηγίες χρήσης

### Εγκατάσταση του docker engine
<details>
<summary>Σε Windows</summary>

- Κάντε λήψη του <a href="https://docs.docker.com/docker-for-windows/install/">Docker Desktop Installer</a>.
- Ακολούθως, κάντε διπλό κλικ στο `Docker Desktop Installer.exe` για να εκτελέσετε το πρόγραμμα εγκατάστασης.
- Εν συνεχεία, ακολουθήστε τη διαδικασία εγκατάστασης και περιμένετε μέχρι να ολοκληρωθεί.
- Μετά την ολοκλήρωση της διαδικασίας εγκατάστασης, κάντε κλικ στο `Close and restart`.

</details>

<details>
<summary>Σε Linux (για διανομές βασισμένες στο Ubuntu)</summary>

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

### Τρέξιμο του docker container
Εκτελέστε την ακόλουθη εντολή στη γραμμή εντολών.

    docker run -p 5000:5000 -d --name InstaUnFollowers aviolaris/instaunfollowers:latest

### Χρήση της εφαρμογής
Πλοηγηθείτε στη διεύθυνση: http://localhost:5000.

Κατεβάστε το `Instagram Information File` (σε HTML μορφή) από <a href="https://accountscenter.instagram.com/info_and_permissions/dyi/">εδώ</a> και μεταφορτώστε το στην παρούσα web εφαρμογή ώστε να λάβετε άμεσα τη λίστα με όλους τους unfollowers του λογαριασμού σας, χωρίς να σταλεί κανένα απολύτως request στους διακομιστές του Instagram.

<img width="1096" alt="preview" src="https://github.com/aviolaris/instaunfollowers/assets/48277853/0d75f2d1-e37b-4927-96cc-eb4149d4051c">

## Deployment

### <a href="https://docs.docker.com/engine/install/">Με χρήση Docker</a>

Χτίσιμο του Docker image:
    
    docker image build --no-cache -t instaunfollowers .
    
Τρέξιμο the Docker container:

    docker run -p 5000:5000 -d --name InstaUnFollowers instaunfollowers

### <a href="https://docs.docker.com/compose/install/">Με χρήση Docker Compose</a>

Χτίσιμο του Docker image και τρέξιμο του Docker container:

    docker-compose up --build -d --force-recreate

## Stack

<img width="250" alt="stack" src="https://user-images.githubusercontent.com/48277853/202203031-3351b2bf-7a20-4748-a081-325bfd9e2038.png">

## Υποστήριξη
| :coffee: | ΟΧΙ    | :star: | ΝΑΙ  |
| :---     | :----: | :----: | ---: |

## Αποποίηση ευθυνών
- Τα εμπορικά σήματα και οι εμπορικές ονομασίες ανήκουν στους αντίστοιχους κατόχους τους. Όλες οι αναφορές σε εταιρείες και ονόματα υπηρεσιών που χρησιμοποιούνται σε αυτό το αποθετήριο είναι για σκοπούς ταυτοποίησης αυτών και μόνο.  

## Πνευματικά δικαιώματα

- Το εικονίδιο του Instagram σχεδιάστηκε από το <a href="https://www.flaticon.com/free-icons/instagram">Freepik - Flaticon</a>.
- Το εικονίδιο του λογότυπου της εφαρμογής σχεδιάστηκε από τον Björn Andersson του <a href="https://thenounproject.com/browse/icons/term/follow/" target="_blank">Noun Project</a>.
- Η γραμματοσειρά του λογότυπου της εφαρμογής σχεδιάστηκε από το <a href="https://www.sudtipos.com/">Sudtipos</a> με άδεια χρήσης <a href="https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=ofl">Open Font License</a>.

## Δημοσιότητα

<a href="https://iguru.gr/instaunfollowers-nomimos-instagram-unfollower-tracker/"><img width="150" alt="preview" src="https://user-images.githubusercontent.com/48277853/206516969-4b48a927-33da-40f2-a161-fd521a094345.jpg"></a> <a href="https://digiworld.gr/2022/12/07/instaunfollowers-%CE%BF-%CE%BD%CF%8C%CE%BC%CE%B9%CE%BC%CE%BF%CF%82-instagram-unfollower-tracker/"><img width="150" alt="preview" src="https://user-images.githubusercontent.com/48277853/206516983-765da894-6cb1-4ab6-997b-0940d2780c53.jpg"></a>

## Αδεια χρήσης

<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.el"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br/><a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.el">[Creative Commons] (Αναφορά Δημιουργού-Μη Εμπορική Χρήση-Όχι Παράγωγα Έργα 4.0 Διεθνές)</a>.