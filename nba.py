from os import times
from time import time
from selenium import webdriver
import json
import codecs
import sys
import time
import os.path
import platform

conferencia = {}
conferencia["conferencia_leste"] = []
conferencia["conferencia_oeste"] = []
so = platform.system()

#================================================
# Entra na página selecionada sem abrir o navegador.
options = webdriver.ChromeOptions()
options.add_argument("--headless")
if so == 'Windows':
    driver = webdriver.Chrome(".\\chromedriver\\chromedriver_windows.exe", chrome_options=options)
elif so == 'Linux':
    driver = webdriver.Chrome(".\\chromedriver\\chromedriver_linux.exe", chrome_options=options)
else:
    print("Sistema Operacional não reconhecido.")
driver.get("https://www.espn.com.br/nba/classificacao/_/ordenar/wins/dir/desce")

#================================================
# Função que capta e cria um dicionário com os
# elementos da tabele de conferência leste.
def leste():

    #================================================
    # Capta todos os elementos necessários da tabela leste.
    table_times = driver.find_elements_by_class_name('Table--align-right')[0]
    table_dados = driver.find_elements_by_class_name('Table--align-right')[1]
    tbody_times = table_times.find_element_by_tag_name('tbody')
    tbody_dados = table_dados.find_element_by_tag_name('tbody')
    trs_times = tbody_times.find_elements_by_tag_name('tr')
    trs_dados = tbody_dados.find_elements_by_tag_name('tr')

    #================================================
    # For que seleciona apenas os textos encontrados
    # nas tabelas captadas, depois cria um dicionário
    # com os elementos selecionados. 
    for x, tr in zip(trs_times,trs_dados):

        times = x.find_elements_by_tag_name('td')[0].get_attribute('innerText')
        num_vitorias = tr.find_elements_by_tag_name('td')[0].get_attribute('innerText')
        num_derrotas = tr.find_elements_by_tag_name('td')[1].get_attribute('innerText')
        porcentagem_vitoria = tr.find_elements_by_tag_name('td')[2].get_attribute('innerText')
        jogos_atras = tr.find_elements_by_tag_name('td')[3].get_attribute('innerText')
        casa = tr.find_elements_by_tag_name('td')[4].get_attribute('innerText')
        visitantes = tr.find_elements_by_tag_name('td')[5].get_attribute('innerText')
        recordes_div = tr.find_elements_by_tag_name('td')[6].get_attribute('innerText')
        marca_conf = tr.find_elements_by_tag_name('td')[7].get_attribute('innerText')
        pontos_a_favor = tr.find_elements_by_tag_name('td')[8].get_attribute('innerText')
        pontos_contra = tr.find_elements_by_tag_name('td')[9].get_attribute('innerText')
        saldo_pontos = tr.find_elements_by_tag_name('td')[10].get_attribute('innerText')
        sequencia_atual = tr.find_elements_by_tag_name('td')[11].get_attribute('innerText')
        u10 = tr.find_elements_by_tag_name('td')[12].get_attribute('innerText')
        
        dados_l = {                
            "time": times,
            "vitorias": num_vitorias,
            "derrotas": num_derrotas,
            "porcentagem_vit": porcentagem_vitoria,
            "jogos_atras": jogos_atras,
            "casa": casa,
            "visitantes": visitantes,
            "recordes_div": recordes_div,
            "marca_conf": marca_conf,
            "pontos_a_favor": pontos_a_favor,
            "pontos_contra": pontos_contra,
            "saldo_pontos": saldo_pontos,
            "sequencia_atual": sequencia_atual,
            "u10": u10
            }
        times_dados_l = [(times , dados_l)]
        times_dados_dict_l = dict(times_dados_l)
        conferencia['conferencia_leste'].append(times_dados_dict_l)   

#================================================
# Função que capta e cria um dicionário com os
# elementos da tabele de conferência leste.
def oeste():

    #================================================
    # Capta todos os elementos necessários da tabela leste.
    table_times = driver.find_elements_by_class_name('Table--align-right')[2]
    table_dados = driver.find_elements_by_class_name('Table--align-right')[3]
    tbody_times = table_times.find_element_by_tag_name('tbody')
    tbody_dados = table_dados.find_element_by_tag_name('tbody')
    trs_times = tbody_times.find_elements_by_tag_name('tr')
    trs_dados = tbody_dados.find_elements_by_tag_name('tr')

    #================================================
    # For que seleciona apenas os textos encontrados
    # nas tabelas captadas, depois cria um dicionário
    # com os elementos selecionados.
    for x, tr in zip(trs_times,trs_dados):

        #----------------------------------------------------
        time = x.find_elements_by_tag_name('td')[0].get_attribute('innerText')
        times = time.replace("x --\n", "")
        #-----------------------------------------------------
        num_vitorias = tr.find_elements_by_tag_name('td')[0].get_attribute('innerText')
        num_derrotas = tr.find_elements_by_tag_name('td')[1].get_attribute('innerText')
        porcentagem_vitoria = tr.find_elements_by_tag_name('td')[2].get_attribute('innerText')
        jogos_atras = tr.find_elements_by_tag_name('td')[3].get_attribute('innerText')
        casa = tr.find_elements_by_tag_name('td')[4].get_attribute('innerText')
        visitantes = tr.find_elements_by_tag_name('td')[5].get_attribute('innerText')
        recordes_div = tr.find_elements_by_tag_name('td')[6].get_attribute('innerText')
        marca_conf = tr.find_elements_by_tag_name('td')[7].get_attribute('innerText')
        pontos_a_favor = tr.find_elements_by_tag_name('td')[8].get_attribute('innerText')
        pontos_contra = tr.find_elements_by_tag_name('td')[9].get_attribute('innerText')
        saldo_pontos = tr.find_elements_by_tag_name('td')[10].get_attribute('innerText')
        sequencia_atual = tr.find_elements_by_tag_name('td')[11].get_attribute('innerText')
        u10 = tr.find_elements_by_tag_name('td')[12].get_attribute('innerText')


        dados_o = {                
            "time": times,
            "vitorias": num_vitorias,
            "derrotas": num_derrotas,
            "porcentagem_vit": porcentagem_vitoria,
            "jogos_atras": jogos_atras,
            "casa": casa,
            "visitantes": visitantes,
            "recordes_div": recordes_div,
            "marca_conf": marca_conf,
            "pontos_a_favor": pontos_a_favor,
            "pontos_contra": pontos_contra,
            "saldo_pontos": saldo_pontos,
            "sequencia_atual": sequencia_atual,
            "u10": u10
            }
        times_dados_o = [(times , dados_o)]
        times_dados_dict_o = dict(times_dados_o)
        conferencia['conferencia_oeste'].append(times_dados_dict_o)  

#================================================
# Função que converte o dicionário criado para
# um arquivo .json de nome "tabela.json"
def write_json():
    with open(r".\resultados\tabela.json", 'wb') as outfile:
        json.dump(conferencia, codecs.getwriter("utf-8")(outfile))

#================================================
# Da 5 segundos de espera para carregar a página
# no navegador e depois printa se o usuário quer
# ou não atualizar o arquivo .json, caso não queira
# abre o arquivo ja existente para leitura apenas.
time.sleep(5)
if(os.path.exists(r'.\resultados\tabela.json')):
    print("*********************************")
    print("Deseja atualizar a lista?")
    print("*********************************")
    atualizar = input(" S ou N:")
    if str(atualizar).upper() == "S":
        leste()
        oeste()
        write_json()
    elif str(atualizar).upper() == "N":
        with open(r'.\resultados\tabela.json', 'r') as openfile: 
            json_object = json.load(openfile)
    else:
        print("valor invalido")
        sys.exit()
else:
    write_json()


#================================================
# Pergunta quais os filtros o usuário quer usar
# para fazer a leitura do aruivo
print("*********************************")
print("Selecione uma opção para filtrar")
print("(1) filtrar por time")
print("(2) filtrar por times")
print("(3) filtrar por conferencia")
print("(4) Sem filtro(tudo)")
print("(5) Filtrar por atributos gerais")
print("*********************************")
variavel = input("Selecione o filtro:")

#================================================
# Filtro feito para selecionar 1 time e fazer a leitura
if str(variavel) == "1":
    time_selecionado = input("Selecione o time:")
    valor = json_object['conferencia_leste']
    valor2 = json_object['conferencia_oeste']
    for x in valor:
        try:
            print(x[time_selecionado])
        except:
            pass
    for y in valor2:
        try:
            print(y[time_selecionado])
        except:
            pass

#================================================
# Filtro feito para selecionar 1 ou mais times
#para fazer a leitura de todos os parâmetros
elif str(variavel) == "2":
    filtro_times = input("Times separados por ,:").split(",")
    valor = json_object['conferencia_leste']
    valor2 = json_object['conferencia_oeste']
    for x in valor:
        for y in filtro_times:
            try:
                print(x[y])
            except:
                pass
    for x in valor2:
        for y in filtro_times:
            try:
                print(x[y])

            except:
                pass
            
#================================================
# Filtra por conferências Leste ou Oeste              
elif str(variavel) == "3":
    print("conferencia Leste(1) ou Confereincia Oeste(2)")
    filtro_conferencia = input("(1) ou (2)")
    if filtro_conferencia == "1":
        print(json_object['conferencia_leste'])
    elif filtro_conferencia == "2":
        print(json_object['conferencia_oeste'])

#================================================
# Printa o dicionário inteiro sem filtros
elif str(variavel) == "4":
    print(json_object)

#================================================
# Filtra o dicionário de acordo com os dados
# de cada time
elif str(variavel) == "5":
    print("(1) Time\n"
        "(2) Vitórias\n"
        "(3) Derrotas\n"
        "(4) Porcentagem vitórias\n"
        "(5) Jogos atrás\n"
        "(6) Casa\n"
        "(7) Visitantes\n"
        "(8) Recordes da divisão\n"
        "(9) Marca conferência\n"
        "(10) Pontos_a_favor\n"
        "(11) Pontos contra\n"
        "(12) Saldo pontos\n"
        "(13) Sequência atual\n"
        "(14) U10\n")

    dados = input("Selecione o número do atributo:")
    valores_l = json_object['conferencia_leste']
    valores_o = json_object['conferencia_oeste']    
    num = ""
    if dados == '1':
        num += ""
    elif dados == '2':
        num +='vitorias'
    elif dados == '3':
        num += 'derrotas'
    elif dados == '4':
        num += 'porcentagem_vit'
    elif dados == '5':
        num += 'jogos_atras'
    elif dados == "6":
        num += 'casa'
    elif dados == '7':
        num += 'visitantes'
    elif dados == '8':
        num += 'recordes_div'
    elif dados == '9':
        num += 'marca_conf'
    elif dados == '10':
        num += 'pontos_a_favor'
    elif dados == '11':
        num += 'pontos_contra'
    elif dados == '12':
        num += 'saldo_pontos'
    elif dados == '13':
        num += 'sequencia_atual'
    elif dados == '14':
        num += 'u10'
    
    if num == "":
        print("**Conferência Leste**")
        for index, valor_l in enumerate(valores_l):
            for time_l in valor_l:
                print(str(index+1)+"-"+str(valor_l[time_l]['time']))
        print("**Conferência Oeste**")
        for index, valor_o in enumerate(valores_o):
            for time_o in valor_o:
                print(str(index+1)+"-"+str(valor_o[time_o]['time']))
    else: 
        print("**Conferência Leste**")
        for index, valor_l in enumerate(valores_l):
            for time_l in valor_l:
                print(str(index+1)+"-"+str(valor_l[time_l]['time'])+"-"+str(valor_l[time_l][num]))
        print("**Conferência Oeste**")
        for index, valor_o in enumerate(valores_o):
            for time_o in valor_o:
                print(str(index+1)+"-"+str(valor_o[time_o]['time'])+"-"+str(valor_o[time_o][num]))
