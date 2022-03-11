from array import array
from audioop import add
import imp
from multiprocessing.sharedctypes import Value
from os import times
from time import time
from turtle import back
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import codecs
import sys
import teste

conferencia = {}
conferencia["conferencia_leste"] = []
conferencia["conferencia_oeste"] = []


options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.espn.com.br/nba/classificacao/_/ordenar/wins/dir/desce")

def leste():
    table_times = driver.find_elements_by_class_name('Table--align-right')[0]
    table_dados = driver.find_elements_by_class_name('Table--align-right')[1]
    tbody_times = table_times.find_element_by_tag_name('tbody')
    tbody_dados = table_dados.find_element_by_tag_name('tbody')
    trs_times = tbody_times.find_elements_by_tag_name('tr')
    trs_dados = tbody_dados.find_elements_by_tag_name('tr')

    

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
        
        fe = {                
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
            "sequencia_atua": sequencia_atual,
            "u10": u10
            }
        fe2 = [(times , fe)]
        fe3 = dict(fe2)
        conferencia['conferencia_leste'].append(fe3)   

def oeste():
    table_times = driver.find_elements_by_class_name('Table--align-right')[2]
    table_dados = driver.find_elements_by_class_name('Table--align-right')[3]
    tbody_times = table_times.find_element_by_tag_name('tbody')
    tbody_dados = table_dados.find_element_by_tag_name('tbody')
    trs_times = tbody_times.find_elements_by_tag_name('tr')
    trs_dados = tbody_dados.find_elements_by_tag_name('tr')

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


        conferencia["conferencia_oeste"].append({
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
            "sequencia_atua": sequencia_atual,
            "u10": u10
            }) 

def write_json():
    with open(r"C:\projetos\git\Tabela-NBA\fe.json", 'wb') as outfile:
        json.dump(conferencia, codecs.getwriter("utf-8")(outfile))

def print_time():
    valor = json_object['conferencia_leste']
    for index, x in enumerate(valor):
        print(str(index+1)+"-"+(x['time']+"-"+(x['vitorias'])+"-"+(x['derrotas'])))
    print('------------------------------------------------------------------------')
    valor2 = conferencia['conferencia_oeste']
    for index, x in enumerate(valor2):
        print(str(index+1)+"-"+(x['time']+"-"+(x['vitorias'])+"-"+(x['derrotas'])))
    print('------------------------------------------------------------------------')

print("*********************************")
print("Deseja atualizar a lista?")
print("*********************************")
atualizar = input(" S ou N")
if str(atualizar).upper() == "S":
    leste()
    oeste()
    write_json()
elif str(atualizar).upper() == "N":
    with open(r'C:\projetos\git\Tabela-NBA\fe.json', 'r') as openfile: 
        json_object = json.load(openfile)
else:
    print("valor invalido")
    sys.exit()
print("*********************************")
print("Selecione uma opção para filtrar")
print("(1) filtrar por time")
print("(2) filtrar por times")
print("(3) filtrar por conferencia")
print("(4) Sem filtro(tudo)")
print("*********************************")
variavel = input("Selecione o filtro:")

if str(variavel) == "1":
    valor = json_object['conferencia_leste']
    print(valor.index())
    # filtro_time = input("Qual o time:")
elif str(variavel) == "2":
    filtro_times = input("Times separados por /:")
elif str(variavel) == "3":
    print("conferencia Leste(1) ou Confereincia Oeste(2)")
    filtro_conferencia = input("(1) ou (2)")
    if filtro_conferencia == "1":
        print("Conferência Leste:"+json_object['conferencia_leste'])
    elif filtro_conferencia == "2":
        print("Conferência Oeste:"+json_object['conferencia_oeste'])
elif str(variavel) == "4":
    print(json_object)



# valor = json_object['conferencia_leste']
# print(valor['Miami Heat'])
# print('------------------------------------------------------------------------')






