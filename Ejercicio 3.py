import os

def clear():
    if os.name == "nt":
        os.system("cls")
    
personas = {}

while True:
    print("*----------[Menú]---------------*")
    print("1. Alta de contacto")                   
    print("2. Búsqueda de contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Mostrar todos los contactos")
    print("6. Salir")
    print("*-------------------------------*\n")
    
    try:
        ingreso = int(input("Ingrese la opción que desea realizar: "))
        clear()

        if ingreso == 1:
            print("==Alta de contacto==")
            
            try:
                dni = int(input("Ingrese el DNI: "))
    
                if dni in personas:
                    print("Ya existe una persona con ese dni")
    
                else:
                    nombre = input("Ingrese el nombre de la persona: ")    
                    teléfono = int(input("Ingrese el número de teléfono: "))
                    email = input("Ingrese el email: ")   
    
                    personas[dni] = {"nombre" : nombre, "teléfono" : teléfono, "email" : email, "dni": dni}
                    print("Usuario registrado\n")
            
            except ValueError:
                print("Error de ingreso: Debe ingresar un documento.")
                
    
        elif ingreso == 2:
            
            try:
                buscarDni = int(input("Ingrese el DNI del contacto a buscar: "))
    
                if buscarDni in personas:
                    print(f"El contacto se encuentra agendado:")
                    print((personas[buscarDni]))
                else:
                    print("El contacto no se encuentra agendado")
                          
            except ValueError:
                print("Error de ingreso: Debe ingresar un documento.")
                            
                          
        elif ingreso == 3:
            if len(personas) == 0:
                print("No hay contactos para actualizar")
                
            else:
                print("===Actualización de contacto===") 
                for x,y in personas.items():
                    print(x, y)
                print("===========================")   
                 
                 
                try: 
                    actu = int(input("Ingrese el dni del contacto que desea actualizar: "))
    
                    if actu in personas:
                        while True:
                            print("1. Nombre")
                            print("2. Teléfono")
                            print("3. Email")
                            print("4. Volver atrás")
                            
                            
                            try:
                                ingreso = int(input("¿Qué opción desea marcar? (1/2/3/4):  "))
    
                                if ingreso == 1:
                                    nombreNew = input("Ingrese un nuevo nombre: ")
                                    personas[actu]["nombre"] = nombreNew
                                    print("Nombre cambiado con éxito!\n")
    
                                elif ingreso == 2:
                                    teléfonoNew = int(input("Ingrese un nuevo número de teléfono: "))
                                    personas[actu]["teléfono"] = teléfonoNew
                                    print("Teléfono cambiado con éxito!\n")
    
                                elif ingreso == 3:
                                    emailNew = (input("Ingrese un nuevo email: "))
                                    personas[actu]["email"] = emailNew
                                    print("Email cambiado con éxito!\n")
    
                                elif ingreso == 4:
                                    break
                                
                                else:
                                    print("Opción inválida, intente nuevamente")
                                    
                            except ValueError:
                                print("Debe ingresar un número")
               
                except ValueError:
                    print("Error de ingreso: Debe ingresar un documento.")
                    
                    
        elif ingreso == 4:
                if len(personas) == 0:
                        print("No se enuentran usuarios registrados")
    
                else:
                    for x,y in personas.items():
                        print(x , y)
                        
                    try:
                        eliminar = int(input("Ingrese el dni de un usario para dar de baja: "))
    
                        if eliminar in personas:
                            del personas[eliminar]
                            print("Usuario eliminado\n")
                        else:
                            print("El dni es incorrecto o el usuario no se encuentra registrado")
                            
                    except ValueError:
                        print("Error de ingreso: Debe ingresar un documento.")
                
        elif ingreso == 5:
                if len(personas) == 0:
                    print("No hay contactos agendados\n")
                    
                else:
                    print("Contactos:")
                    for x, y in personas.items():
                      print(x, y)
    
        elif ingreso == 6:
            print("Saliendo..\n")
            break
        
        else:
            print("Opcción no válida, intente nuevamente")
            
    except ValueError:
        print("Error de ingreso: Debe ingresar un documento.")