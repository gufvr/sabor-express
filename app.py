import os

restaurants = ['Fino Osteria', 'Vip Sushi']

def show_program_name():
      print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)

def show_options():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurantes')
    print('4. Sair\n')

def close_app():
    os.system('cls')
    print('Fechando a aplicação\n')


def invalid_option():
    print('Opção invalida!\n')
    input('Digite qualquer tecla para voltar ao menu principal')
    main()

def register_new_restaurant():
     os.system('cls')
     print('Cadastro de novos restaurantes\n')
     restaurant_name = input('Digite o nome do restaurante que deseja cadastrar: ')
     restaurants.append(restaurant_name)
     print(f'O restaurante {restaurant_name} foi cadastrado com sucesso!')
     input('\nDigite qualquer tecla para voltar ao menu principal.')
     main()

def list_restaurants():
     os.system('cls')
     print('Listagem de restaurantes\n')
     
     for restaurant in restaurants:
            print(f'• {restaurant}')

     input('\nDigite qualquer tecla para voltar ao menu principal.')
     main()


def choose_option():
    try:
      chosen_option = int(input(f'Escolha um opção: '))

      if chosen_option == 1:
            register_new_restaurant()
      elif chosen_option == 2:
            list_restaurants()
      elif chosen_option == 3:
            print('Ativar restaurante')
      elif chosen_option == 4:
            close_app()
      else:
            invalid_option()
    except:
      invalid_option()

def main():
    os.system('cls')
    show_program_name()
    show_options()
    choose_option()

if __name__ == '__main__':
    main()