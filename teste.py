from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.espn.com.br/nba/classificacao")

driver.quit()





dict = {'carro':
            {'cor':'vermelho',
             'rodas': '4',
             'espelhos':'2'},
        'moto':
            {'cor':'azul',
             'rodas': '2',
             'espelhos':'2'}
        }