@login
Feature: Inicio de sesion
    Background: 
        Given que el usuario esta en la pagina de Login

    @positivo
    Scenario: Login exitoso
        When ingresa el usuario 'standard_user' y el password 'secret_sauce'
        And hace click en el boton de login
        Then deberia ingresar al inventario
    
    @negativo
    Scenario: Login invalido con password incorrecto
        When ingresa el usuario 'standard_user' y el password '12345'
        And hace click en el boton de login
        Then deberia ver el mensaje de error 'Epic sadface: Username and password do not match any user in this service'

    @negativo @regression
    Scenario Outline: Login invalidos con diferentes opciones
        When ingresa el usuario '<usuario>' y el password '<password>'
        And hace click en el boton de login
        Then deberia ver el mensaje de error '<mensaje_error>'

        Examples:
            | usuario         | password       | mensaje_error                                                                 |
            | standard_user   | 12345          | Epic sadface: Username and password do not match any user in this service     |
            | estandar_user   | secret_sauce   | Epic sadface: Username and password do not match any user in this service     |
            | VACIO           | secret_sauce   | Epic sadface: Username is required                                            |
            | standard_user   | VACIO          | Epic sadface: Password is required                                            |

