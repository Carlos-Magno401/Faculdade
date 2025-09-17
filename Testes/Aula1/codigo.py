import pyautogui
import time
import pandas

# pyautogui.click  clica em algum lugar
# pyautogui.press  aperta 1 tecla
# pyautogui.write  escreve um texto
# pyautogui.hotkay aperta uma combinacao de teclas

pyautogui.PAUSE = 0.5 # da um pause de X segundos pra cada comando

# vai abrir o site
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(1) # vai esperar 1 segundos antes de fazer o proximo comando

# fazer login
pyautogui.click(x=437, y=377)
pyautogui.write("teste@gmail.com") # fazer login email

pyautogui.click(x=432, y=468) # fazer login senha
pyautogui.write("12341234938274983279487398274284729379848972498987497832949832498723974987329874239874978329874298")

pyautogui.click(x=720, y=538) # clica em login

# ou pyautogui.press("tab")
#    pyautogui.press("enter")

tabela = pandas.read_csv("d:\Estudando\Testes\Aula1\produtos.csv")


for linha in tabela.index:
    pyautogui.click(x=426, y=256)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    
    obs = str(tabela.loc[linha, "obs"]) 
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(100000)     # vai usar o scroll até o começo do site


