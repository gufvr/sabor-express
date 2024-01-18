import os

restaurants = [{'Nome':'Praça', 'Categoria':'Fast Food', 'Ativo':False}, 
               {'Nome':'Fino Osteria', 'Categoria':'Culinária Italiana', 'Ativo':True}, 
               {'Nome':'Vip Sushi', 'Categoria':'Culinária Japonesa', 'Ativo':False}]

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
    show_subtitles('Fechando a aplicação')

def back_to_main_menu():
    input('\nDigite qualquer tecla para voltar ao menu principal')
    main()

def invalid_option():
    print('Opção invalida!')
    back_to_main_menu()

def show_subtitles(text):
     os.system('cls')
     print(text)
     print('')

def register_new_restaurant():
     show_subtitles('Cadastro de novos restaurantes')

     restaurant_name = input('Digite o nome do restaurante que deseja cadastrar: ')
     category = input(f'Digite o nome da categoria do estabelecimento {restaurant_name}: ')
     restaurant_data = {'Nome':restaurant_name, 'Categoria':category, 'Ativo':False}
     restaurants.append(restaurant_data)
     print(f'O restaurante {restaurant_name} foi cadastrado com sucesso!')
     back_to_main_menu()

def list_restaurants():
     show_subtitles('Listagem de restaurantes')
     
     for restaurant in restaurants:
            name = restaurant['Nome']
            category = restaurant['Categoria']
            is_active = restaurant['Ativo']
            print(f'• {name} | {category} | {is_active}')

     back_to_main_menu()

def restaurant_state_toggle():
    show_subtitles('Alternando estado do restaurante')

    restaurant_name = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurant_found = False

    for restaurant in restaurants:
         if restaurant_name == restaurant['Nome']:
              restaurant_found = True
              restaurant['Ativo'] = not restaurant['Ativo']

              message = f'O restaurante {restaurant_name} foi ativado com sucesso.' if restaurant['Ativo'] else f'O restaurante {restaurant_name} foi desativado com sucesso.'
              print(message)
              
    if not restaurant_found:
         print('O restaurante não foi encontrado.')

    back_to_main_menu()

def choose_option():
    try:
      chosen_option = int(input(f'Escolha um opção: '))

      if chosen_option == 1:
            register_new_restaurant()
      elif chosen_option == 2:
            list_restaurants()
      elif chosen_option == 3:
            restaurant_state_toggle()
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