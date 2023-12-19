class MyLocators():
    driver_path = './webdrivers/chromedriver'
    URL = 'https://industriamaquiladora.com/index.php'
    results_csv = './Evidences/result.csv'
    
    #Popup
    xpath_popup_title = "/html/body/div[4]/div/div/div[1]/h5/strong"
    xpath_button_close_popup = "/html/body/div[4]/div/div/div[1]/button"
    
    xpath_menu = "/html/body/section[1]/nav/div[2]/div[2]/ul/li[4]"
    link_text_directorio = "DIRECTORIO"
    link_text_proveedores = "PROVEEDORES"
    id_customer_name = "nombre"
    
    class_for_customer_information = "first-column"
    class_for_item_row_customer = "row"
    class_for_item_row_key = "col-md-4"
    class_for_item_row_value = "col-md-8"
    
    name_user_name = "user-name"
    name_user_password = "password"
    
    