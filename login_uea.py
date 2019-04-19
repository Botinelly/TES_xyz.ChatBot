from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("headless")

drive = webdriver.Chrome(chrome_options=options)

EMAIL ="rafds.snf@uea.edu.br"
SENHA = "1515310023"

NUM_PROTOCOLO = "201900006908"
SENHA_PROTOCOLO = "d122af"

URL_HORARIOS = "http://177.66.10.35/lyceump/aonline/horario.asp"
URL_NOTAS = "http://177.66.10.35/lyceump/aonline/notas_freq.asp"
URL_PROTOCOLO = "http://www1.uea.edu.br/modulo/login/protocolo.php"

XPATH_HORARIOS = "//*[@id='ctnTabPagina2']/table/tbody/tr/td/table[2]"
XPATH_NOTAS = "//*[@id='ctnTabPagina2']/table/tbody/tr/td/table"

def uea_login():
    drive.get("http://www2.uea.edu.br/modulo/login/lyceum2.php")
    drive.find_element_by_id("email").send_keys(EMAIL)
    drive.find_element_by_id("senha").send_keys(SENHA)
    drive.find_element_by_class_name("btn").click()
    time.sleep(5)

def uea_horario():
    drive.get(URL_HORARIOS)
    print(drive.current_url)

    xpath_horarios = drive.find_elements_by_xpath(XPATH_HORARIOS)[0]
    lista_de_horarios = xpath_horarios.text
    print(lista_de_horarios)

def uea_notas():
    drive.get(URL_NOTAS)
    print(drive.current_url)

    xpath_notas = drive.find_elements_by_xpath(XPATH_NOTAS)[0]
    lista_de_notas = xpath_notas.text
    print(lista_de_notas)

def uea_protocolo():
    drive.get(URL_PROTOCOLO)
    print(drive.current_url)

    drive.find_element_by_id("procId").send_keys(NUM_PROTOCOLO)
    drive.find_element_by_id("password").send_keys(SENHA_PROTOCOLO)
    drive.find_element_by_class_name("btn").click()
    time.sleep(5)

    info_proc = drive.find_element_by_class_name("panel")
    info = info_proc.text
    print(info)

uea_login()
uea_horario()
uea_notas()
uea_protocolo()
