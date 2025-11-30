nom = input("\nQuin es el teu nom? ")                         # Demana el nom a l'usuari
cognom = input("Quin es el teu cognom? ")                   # Demana el cognom a l'usuari
nom_avatar = input("Indica el nom del teu avatar: ")        # Demana el nom de l'avatar
edat_avatar = input("Indica l'edat del teu avatar: ")       # Demana l'edat de l'avatar
nivell_intelligencia = input("Indica el nivell d'intelligencia del teu avatar: ")               # Demana el nivell d'intelligencia
nivell_velocitat = input("Indica el nivell de velocitat del teu avatar: ")                      # Demana el nivell de velocitat
nivell_forca = input("Indica el nivell de força del teu avatar: ")                              # Demana el nivell de força
mitjana_stats = (int(nivell_intelligencia) + int(nivell_velocitat) + int(nivell_forca)) / 3     # Calcula la mitjana dels stats
descripcio_avatar = input("Fes una desctipcio del teu avatar: ")                                # Demana una descripcio de l'avatar


# Mostra tota la informacio recollida a la consola
print("\nEl teu nom es:", nom, cognom)
print("El nom del teu avatar es:", nom_avatar)
print("L'edat del teu avatar es:", edat_avatar)
print("El nivell d'intelligencia del teu avatar es:", nivell_intelligencia)
print("El nivell de velocitat del teu avatar es:", nivell_velocitat)   
print("El nivell de força del teu avatar es:", nivell_forca)
print("La mitjana dels stats del teu avatar es:", mitjana_stats)
print("La descripcio del teur avatar es:", descripcio_avatar)
