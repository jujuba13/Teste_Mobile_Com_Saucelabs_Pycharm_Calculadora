
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pytest

caps = {}
caps["platformName"] = "Android"
caps["appium:platformVersion"] = "9.0"
caps["browserName"] = ""
caps["appium:appiumVersion"] = "1.22.3"
caps["appium:deviceName"] = "Samsung Galaxy S9 FHD GoogleAPI Emulator"
caps["appium:deviceOrientation"] = "portrait"
caps["appium:app"] = "storage:filename=Calculator_v8.1 (403424005)_apkpure.com.apk"
caps["appium:appPackage"] = "com.google.android.calculator"
caps["appium:apppActivity"] = "com.android.calculator2.Calculator"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["sauce:options"] = {"name":"Appium Desktop Session -- Apr 23, 2022 11:22 AM"}
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

# Acionador do script/código
if __name__ == '__main__':

  #  def testar_somar_dois_numeros():
        # Conexão com o Sauce Labs, aponta o datacenter, meu usuário e chave

        driver = webdriver.Remote("https://verteste:b24e7213-bbbc-4db3-99a8-279310e75425@ondemand.us-west-1.saucelabs.com:443/wd/hub", caps)

        resultado_esperado = '13'


       # Realiza a conta
        botao_8 = driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/digit_8")
        botao_8.click()
        botao_somar = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="plus")
        botao_somar.click()
        botao_5 = driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/digit_5")
        botao_5.click()
        botao_Igual = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="equals")
        botao_Igual.click()
        dysplay_Resultado = driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/result_final")

        print(f'resultado final = {dysplay_Resultado.text} \n resultado esperado = {resultado_esperado}')
        assert dysplay_Resultado.text == resultado_esperado

        driver.quit()
