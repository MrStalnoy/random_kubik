import random

min = 1
max = 6
def main():
   again="Д"
   while again == "д" or again == "Д":
      print("Бросаем кубики...")
      print('Значение граней:')
      print(random.randint(min,max))
      print(random.randint(min,max))
      again = input('Бросить кубики еще раз? (д=да):')
main()