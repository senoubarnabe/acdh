from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage, BadHeaderError
from smtplib import SMTPException

def index(request):
    return render(request, "templates/index.html")

def postuler_views(request):
    if request.method == 'POST':
        # Récupération des données du formulaire
        choixOffre = request.POST.get("choixOffre")
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        age = request.POST.get("age")
        profession = request.POST.get("profession")
        residence = request.POST.get("residence")
        nationalite = request.POST.get("nationalite")
        lieuNaissance = request.POST.get("lieuNaissance")
        dateNaissance = request.POST.get("dateNaissance")
        sexe = request.POST.get("sexe")
        tel = request.POST.get("tel")
        photo = request.FILES.get("photo")
        email = request.POST.get("email")
        poids = request.POST.get("poids")
        taille = request.POST.get("taille")
        groupesang = request.POST.get("groupesang")
        situationmatri = request.POST.get("situationmatri")
        nombreenfants = request.POST.get("nombreenfants")
        comptebancaire = request.POST.get("comptebancaire")
        precibanque = request.POST.get("precibanque")
        codePostal = request.POST.get("codePostal")
        adresse = request.POST.get("adresse")
        sante = request.POST.get("sante")
        npasseport = request.POST.get("npasseport")
        photoPasseport = request.FILES.get("photoPasseport")
        idCard = request.POST.get("idCard")
        photoID = request.FILES.get("photoID")
        choixdetravail = request.POST.get("choixdetravail")
        d_travail = request.POST.get("d_travail")
        motifs_voyage = request.POST.getlist("motifVoyage[]")
        moyenPaiement = request.POST.get("moyenPaiement")
        
        # Contenu de l'email
        subject = f"Nouveau Message de {nom} {prenom}"
        body = f"""
            Choix d'offre : {choixOffre}
            Nom : {nom}
            Prenom : {prenom}
            Age : {age}
            Profession : {profession}
            Residence : {residence}
            Nationalite : {nationalite}
            Lieu De Naissance : {lieuNaissance}
            Date DeNaissance : {dateNaissance}
            Sexe : {sexe}
            Telephone : {tel}
            Email : {email}
            Poids : {poids}
            Taille : {taille}
            Groupe Sanguin : {groupesang}
            Situation Matrimoniale : {situationmatri}
            Nombre d'enfants en charge : {nombreenfants}
            Possession De Compte Bancaire : {comptebancaire}
            Type De Banque : {precibanque}
            Code postal : {codePostal}
            Adresse : {adresse}
            Sante : {sante}
            N° de Passeport : {npasseport}
            N° ID CARD : {idCard}
            Choix de travail au Canada : {choixdetravail}
            Durée de travail : {d_travail}
            Motifs de Voyage : {", ".join(motifs_voyage)}
            Moyen De Paiement : {moyenPaiement}

            Photo : {photo.name if photo else 'Aucune'}
            Photo De Passeport : {photoPasseport.name if photoPasseport else 'Aucune'}
            Photo ID : {photoID.name if photoID else 'Aucune'}
        """

        from_email = 'test@example.com'  # Adresse e-mail fictive pour les tests
        recipient_list = ["acdhservice4@gmail.com"]

        # Création de l'EmailMessage pour permettre les pièces jointes
        email_message = EmailMessage(
            subject,
            body,
            from_email,
            recipient_list
        )

        # Ajout des fichiers en pièces jointes, si fournis
        if photo:
            email_message.attach(photo.name, photo.read(), photo.content_type)
        if photoPasseport:
            email_message.attach(photoPasseport.name, photoPasseport.read(), photoPasseport.content_type)
        if photoID:
            email_message.attach(photoID.name, photoID.read(), photoID.content_type)

        # Envoi de l'email avec gestion des erreurs
        try:
            email_message.send()
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        except SMTPException as e:
            return HttpResponse(f'SMTP error occurred: {str(e)}')
        except Exception as e:
            return HttpResponse(f'An error occurred: {str(e)}')

        # Redirection avec confirmation
        return redirect(reverse('confirmation') + f'?nom={nom}&prenom={prenom}&email={email}')

    return render(request, "pos.html")


def temo_views(request):
    return render(request, "temo.html")

def propos_views(request):
    return render(request, "propos.html")


def confirmation_views(request: HttpRequest):
    nom = request.GET.get('nom')
    prenom = request.GET.get('prenom')
    email = request.GET.get('email')

    context = {'nom':nom , 'prenom':prenom , 'email': email}

    return render(request, "confirmation.html", context)