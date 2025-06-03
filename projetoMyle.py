from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://demoblaze.com/")
    time.sleep(3)

    # Cenário 1: Cadastro com email e senha válidos

    #Dado que eu acesso o site [https://demoblaze.com/]
    #Eu clico no botão "Sign up" identificado por [id="signin2"] (abre a modal de cadastro)
    #E preencho o campo "Username" do [id="sign-username"] com [Ravena2025]
    #E preencho o campo "Password" do [id="sign-password"] com [sara2023]
    #Quando clico no botão "Sign up" identificado por [class="btn btn-primary" e texto "Sign up"]
    #Então o sistema deve chamar no JavaScript a função "Sign up successful." (exibir mensagem de sucesso)

    btn_sign_up = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "signin2")))
    btn_sign_up.click()
    time.sleep(2)
    input_user = driver.find_element(By.ID, "sign-username")
    input_user.clear()
    input_user.send_keys("Ravena2025")

    input_pass = driver.find_element(By.ID, "sign-password")
    input_pass.clear()
    input_pass.send_keys("sara2023")

    btn_confirm = driver.find_element(By.XPATH, "//button[contains(@class,'btn') and contains(text(),'Sign up')]")
    btn_confirm.click()
    time.sleep(3)

    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    text1 = alert.text
    alert.accept()
    time.sleep(2)

    driver.execute_script("$('#signInModal').modal('hide');")
    WebDriverWait(driver, 5).until(EC.invisibility_of_element((By.ID, "signInModal")))
    time.sleep(1)

    # Cenário 2: Cadastro com campo de email vazio

    #Eu clico no botão "Sign up" identificado por [id="signin2"] (abre a modal de cadastro)
    #E deixo o campo "Username" do [id="sign-username"] vazio
    #E preencho o campo "Password" do [id="sign-password"] com [sara2023]
    #Quando clico no botão "Sign up" identificado por [class="btn btn-primary" e texto "Sign up"]
    #Então o sistema deve exibir uma mensagem de erro indicando que o campo "Username" é obrigatório

    btn_sign_up = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "signin2")))
    btn_sign_up.click()
    time.sleep(2)

    input_user = driver.find_element(By.ID, "sign-username")
    input_user.clear()
    input_user.send_keys("")

    input_pass = driver.find_element(By.ID, "sign-password")
    input_pass.clear()
    input_pass.send_keys("sara2023")

    btn_confirm = driver.find_element(By.XPATH, "//button[contains(@class,'btn') and contains(text(),'Sign up')]")
    btn_confirm.click()
    time.sleep(3)

    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    text2 = alert.text
    alert.accept()
    time.sleep(2)

    driver.execute_script("$('#signInModal').modal('hide');")
    WebDriverWait(driver, 5).until(EC.invisibility_of_element((By.ID, "signInModal")))
    time.sleep(1)

    # Cenário 3: Cadastro com senha vazia

    #Eu clico no botão "Sign up" identificado por [id="signin2"] (abre a modal de cadastro)
    #E preencho o campo "Username" do [id="sign-username"] com [Ravena2025]
    #E deixo o campo "Password" do [id="sign-password"] vazio
    #Quando clico no botão "Sign up" identificado por [class="btn btn-primary" e texto "Sign up"]
    #Então o sistema deve exibir uma mensagem de erro informando que o campo "Password" é obrigatório

    btn_sign_up = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "signin2")))
    btn_sign_up.click()
    time.sleep(2)

    input_user = driver.find_element(By.ID, "sign-username")
    input_user.clear()
    input_user.send_keys("Ravena2025")

    input_pass = driver.find_element(By.ID, "sign-password")
    input_pass.clear()
    input_pass.send_keys("")

    btn_confirm = driver.find_element(By.XPATH, "//button[contains(@class,'btn') and contains(text(),'Sign up')]")
    btn_confirm.click()
    time.sleep(3)

    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    text3 = alert.text
    alert.accept()
    time.sleep(2)

    driver.execute_script("$('#signInModal').modal('hide');")
    WebDriverWait(driver, 5).until(EC.invisibility_of_element((By.ID, "signInModal")))
    time.sleep(1)

    # Cenário 4: Login com dados válidos

    #Eu clico no botão "Log in" identificado por [id="login2"] (abre a modal de login)
    #E preencho o campo "Username" do [id="loginusername"] com [Ravena2025]
    #E preencho o campo "Password" do [id="loginpassword"] com [sara2023]
    #Quando clico no botão "Log in" identificado por [class="btn btn-primary" e texto "Log in"]
    #Então o sistema deve permitir o acesso e exibir o nome do usuário logado na interface

    btn_log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login2")))
    btn_log_in.click()
    time.sleep(2)

    input_user_login = driver.find_element(By.ID, "loginusername")
    input_user_login.clear()
    input_user_login.send_keys("paulinha")

    input_pass_login = driver.find_element(By.ID, "loginpassword")
    input_pass_login.clear()
    input_pass_login.send_keys("test123")

    btn_confirm_login = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    btn_confirm_login.click()
    time.sleep(3)

    user_logged = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "nameofuser"))
    )
    text4 = user_logged.text

    driver.execute_script("$('#logInModal').modal('hide');")
    WebDriverWait(driver, 5).until(EC.invisibility_of_element((By.ID, "logInModal")))
    time.sleep(1)

    # Cenário 5: Login com username incorreto

    #Eu clico no botão "Log in" identificado por [id="login2"] (abre a modal de login)
    #E preencho o campo "Username" do [id="loginusername"] com [EmailIncorreto123]
    #E preencho o campo "Password" do [id="loginpassword"] com [sara2023]
    #Quando clico no botão "Log in" identificado por [class="btn btn-primary" e texto "Log in"]
    #Então o sistema deve exibir uma mensagem de erro informando que o email está incorreto

    logout_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "logout2")))
    logout_btn.click()
    time.sleep(2)

    btn_log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login2")))
    btn_log_in.click()
    time.sleep(2)

    input_user = driver.find_element(By.ID, "loginusername")
    input_user.clear()
    input_user.send_keys("emylli2008")  # usuário incorreto

    input_pass = driver.find_element(By.ID, "loginpassword")
    input_pass.clear()
    input_pass.send_keys("emylli2020")

    btn_confirm_login = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    btn_confirm_login.click()
    time.sleep(3)

    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    text5 = alert.text
    alert.accept()
    time.sleep(1)

    driver.execute_script("$('#logInModal').modal('hide');")
    WebDriverWait(driver, 5).until(EC.invisibility_of_element((By.ID, "logInModal")))
    time.sleep(1)


    #Cenário 6: Login correto e senha errada

    #Eu clico no botão "Log in" identificado por [id="login2"] (abre a modal de login)
    #E preencho o campo "Username" do [id="loginusername"] com [Ravena2025]
    #E preencho o campo "Password" do [id="loginpassword"] com [senhaErrada123]
    #Quando clico no botão "Log in" identificado por [class="btn btn-primary" e texto "Log in"]
    #Então o sistema deve exibir uma mensagem de erro informando que a senha está incorreta

    btn_log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login2")))
    btn_log_in.click()
    time.sleep(2)

    input_user = driver.find_element(By.ID, "loginusername")
    input_user.clear()
    input_user.send_keys("Japa123")

    input_pass = driver.find_element(By.ID, "loginpassword")
    input_pass.clear()
    input_pass.send_keys("senha errada123")  # senha incorreta

    btn_confirm_login = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    btn_confirm_login.click()
    time.sleep(3)

    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    text6 = alert.text
    alert.accept()
    time.sleep(1)

    driver.execute_script("$('#logInModal').modal('hide');")
    WebDriverWait(driver, 5).until(EC.invisibility_of_element((By.ID, "logInModal")))
    time.sleep(1)

    #Cenário 7: Login com email preenchido e senha vazia

    #Eu clico no botão "Log in" identificado por [id="login2"] (abre a modal de login)
    #E preencho o campo "Username" do [id="loginusername"] com [Ravena2025]
    #E deixo o campo "Password" do [id="loginpassword"] vazio
    #Quando clico no botão "Log in" identificado por [class="btn btn-primary" e texto "Log in"]
    #Então o sistema deve exibir uma mensagem de erro informando que o campo "Password" é obrigatório

    btn_log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login2")))
    btn_log_in.click()
    time.sleep(2)

    input_user = driver.find_element(By.ID, "loginusername")
    input_user.clear()
    input_user.send_keys("Japa123")

    input_pass = driver.find_element(By.ID, "loginpassword")
    input_pass.clear()
    input_pass.send_keys("")  # senha vazia

    btn_confirm_login = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    btn_confirm_login.click()
    time.sleep(3)

    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    text7 = alert.text
    alert.accept()
    time.sleep(1)

    driver.execute_script("$('#logInModal').modal('hide');")
    WebDriverWait(driver, 5).until(EC.invisibility_of_element((By.ID, "logInModal")))
    time.sleep(1)

    #Cenário 8: Login com email vazio e senha preenchida

    #Eu clico no botão "Log in" identificado por [id="login2"] (abre a modal de login)
    #E deixo o campo "Username" do [id="loginusername"] vazio
    #E preencho o campo "Password" do [id="loginpassword"] com [sara2023]
    #Quando clico no botão "Log in" identificado por [class="btn btn-primary" e texto "Log in"]
    #Então o sistema deve exibir uma mensagem de erro informando que o campo "Username" é obrigatório

    btn_log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login2")))
    btn_log_in.click()
    time.sleep(2)

    input_user = driver.find_element(By.ID, "loginusername")
    input_user.clear()
    input_user.send_keys("")  # login vazio

    input_pass = driver.find_element(By.ID, "loginpassword")
    input_pass.clear()
    input_pass.send_keys("emylli123")

    btn_confirm_login = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    btn_confirm_login.click()
    time.sleep(3)

    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    text8 = alert.text
    alert.accept()
    time.sleep(1)

    driver.execute_script("$('#logInModal').modal('hide');")
    WebDriverWait(driver, 5).until(EC.invisibility_of_element((By.ID, "logInModal")))
    time.sleep(1)


    #Cenário 9: Login com email e senha que não foram cadastrados

    #Eu clico no botão "Log in" identificado por [id="login2"] (abre a modal de login)
    #E preencho o campo "Username" do [id="loginusername"] com [usuarioInexistente]
    #E preencho o campo "Password" do [id="loginpassword"] com [senhaIncorreta123]
    #Quando clico no botão "Log in" identificado por [class="btn btn-primary" e texto "Log in"]
    #Então o sistema deve exibir uma mensagem de erro informando que o usuário não está cadastrado ou as credenciais são inválidas

    btn_log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login2")))
    btn_log_in.click()
    time.sleep(2)

    input_user = driver.find_element(By.ID, "loginusername")
    input_user.clear()
    input_user.send_keys("naocadastrado123")  # login não cadastrado

    input_pass = driver.find_element(By.ID, "loginpassword")
    input_pass.clear()
    input_pass.send_keys("naocadastrado123")

    btn_confirm_login = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    btn_confirm_login.click()
    time.sleep(3)

    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    text9 = alert.text
    alert.accept()
    time.sleep(1)

    driver.execute_script("$('#logInModal').modal('hide');")
    WebDriverWait(driver, 5).until(EC.invisibility_of_element((By.ID, "logInModal")))
    time.sleep(1)

    #Cenário 10: Login com os dois campos vazios

    #Eu clico no botão "Log in" identificado por [id="login2"] (abre a modal de login)
    #E deixo o campo "Username" do [id="loginusername"] vazio
    #E deixo o campo "Password" do [id="loginpassword"] vazio
    #Quando clico no botão "Log in" identificado por [class="btn btn-primary" e texto "Log in"]
    #Então o sistema deve exibir uma mensagem de erro informando que os campos "Username" e "Password" são obrigatórios

    btn_log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login2")))
    btn_log_in.click()
    time.sleep(2)

    input_user = driver.find_element(By.ID, "loginusername")
    input_user.clear()
    input_user.send_keys("")  # login vazio

    input_pass = driver.find_element(By.ID, "loginpassword")
    input_pass.clear()
    input_pass.send_keys("")  # senha vazia


    btn_confirm_login = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    btn_confirm_login.click()
    time.sleep(3)

    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    text10 = alert.text
    alert.accept()
    time.sleep(1)

    driver.execute_script("$('#logInModal').modal('hide');")
    WebDriverWait(driver, 5).until(EC.invisibility_of_element((By.ID, "logInModal")))
    time.sleep(1)

    # Exibir Resultados
    print("\n=========== RESULTADOS ===========")
    print(f"Cenário 1 - Cadastro com dados válidos: {'✅' if text1 == 'Sign up successful.' else '❌'} ({text1})")
    print(f"Cenário 2 - Cadastro com username vazio: {'✅' if text2 != 'Sign up successful.' else '❌'} ({text2})")
    print(f"Cenário 3 - Cadastro com senha vazia: {'✅' if text3 != 'Sign up successful.' else '❌'} ({text3})")
    print(f"Cenário 4 - Login com dados válidos: {'✅' if 'Welcome' in text4 else '❌'} ({text4})")
    print(f"Cenário 5 - Login com username incorreto: {'✅' if 'User does not exist.' in text5 or 'Wrong password.' in text5 else '❌'} ({text5})")
    print(f"Cenário 6 - Login com senha incorreto: {'✅' if text6 == 'Wrong password.' else '❌'} ({text6})")
    print(f"Cenário 7 - Login com senha vazia: {'✅' if text7 == 'Please fill the Password.' else '❌'} ({text7})")
    print(f"Cenário 8 - Login com usuario vazio: {'✅' if text8 == 'Please fill the Username.' else '❌'} ({text8})")
    print(f"Cenário 9 - Login e senha não cadastrados: {'✅' if text9 == 'User and password does not match.' else '❌'} ({text9})")
    print(f"Cenário 10 - Login e senha vazia: {'✅' if text10 == 'Please fill User and Password.' else '❌'} ({text10})")
    print("===================================")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
finally:
    driver.quit()
print("============Programa Finalizado===================")