from girafa import Girafa

girafa = Girafa("Melmam", 4.15, "Amarela e Marrom", 32, "Africa Central")
girafa2 = Girafa("Gepeto", 5.15, "Amarela e Verde", 29, "Africa Central")

print(girafa.nome)
girafa2.comer('folhas')
girafa2.comer('folhas')
girafa2.comer('folhas')

girafa2.fome()
girafa2.andar()
girafa2.respira()

filhote = girafa2.reproduz(girafa)

print(filhote.nome)
filhote.fome()
filhote.andar()
filhote.respira()
