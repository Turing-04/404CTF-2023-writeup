# Le Tour de France - Intro, 100 points

<img src="chall.png" width=500>

On a une image prise sur l'autoroute à notre disposition et c'est parti pour une petite partie de GeoGuesser.

<img src="./Le_Tour_de_France.png" width=500>

On note la mention du quartier de Beaune (Saint Nicolas), nous sommes donc sur l'A6, proche de la sortie pour la ville de Beaune. 

Dès que l'on a trouvé une position qui semble cohérente avec les indications trouvées sur le paneau et on passe en google streetview. On tombe assez rapidement exactement à l'endroit où a été prise la photo. 

<img src="./street_view.png" width=500>

Il ne reste plus qu'a récupérer la longitude et la lattitude correspondante (on les trouve dans l'URL).
On pense à bien arrondir les coordonnées au centième et on obtient les valeurs suivantes : `47.02 et 4.87`.

<details>
<summary>Voir le flag :</summary>

***FLAG: 404CTF{47.02,04.87}***
</details>