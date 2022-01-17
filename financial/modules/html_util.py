'''
Created on 2018年11月15日

@author: adidas_001
'''
from modules.all_dto import AllDTO 
class HtmlUtil(object):

    def __init__(self):
        '''
        Constructor
        '''
    def get_element_dto_list(self, elements, count_element):
        data_list = []
        dto = AllDTO()
        i = 0
        for element in elements:
            i += 1
            if i%count_element == 1:
                dto = AllDTO()
                dto.set_element1(element)  
            elif i%count_element == 2:
                dto.set_element2(element)     
            elif i%count_element == 3:
                dto.set_element3(element)    
            elif i%count_element == 4:
                dto.set_element4(element)  
            elif i%count_element == 5:
                dto.set_element5(element)  
            elif i%count_element == 6:
                dto.set_element6(element)  
            elif i%count_element == 7:
                dto.set_element7(element) 
            elif i%count_element == 8:
                dto.set_element8(element) 
            elif i%count_element == 9:
                dto.set_element9(element)  
            elif i%count_element == 10:
                dto.set_element10(element)    
            elif i%count_element == 11:
                dto.set_element11(element)    
            elif i%count_element == 12:
                dto.set_element12(element)    
            elif i%count_element == 13:
                dto.set_element13(element)  
            elif i%count_element == 14:
                dto.set_element14(element)  
            elif i%count_element == 15:
                dto.set_element15(element) 
            elif i%count_element == 16:
                dto.set_element16(element) 
            elif i%count_element == 17:
                dto.set_element17(element)  
            elif i%count_element == 18:
                dto.set_element18(element)
            elif i%count_element == 19:
                dto.set_element19(element)  
            elif i%count_element == 20:
                dto.set_element20(element)  
            elif i%count_element == 21:
                dto.set_element21(element)  
            elif i%count_element == 22:
                dto.set_element22(element)  
            elif i%count_element == 23:
                dto.set_element23(element)      
            elif i%count_element == 24:
                dto.set_element24(element)                
            elif i%count_element == 25:
                dto.set_element25(element)              
            elif i%count_element == 26:
                dto.set_element26(element)              
            elif i%count_element == 27:
                dto.set_element27(element)   
            elif i%count_element == 28:
                dto.set_element28(element) 
            elif i%count_element == 29:
                dto.set_element29(element)        
                
                                          
            if i%count_element == 0   : 
                self.set_last_element(dto, element, count_element) 
                data_list.append(dto)
                
                                                         
#             print(element.get_attribute('innerText'))
        return data_list        
    
    def set_last_element(self, dto, element, count):
        if count == 1:
            dto.set_element1(element)  
        elif count == 2:
            dto.set_element2(element)     
        elif count == 3:
            dto.set_element3(element)    
        elif count == 4:
            dto.set_element4(element)  
        elif count == 5:
            dto.set_element5(element)  
        elif count == 6:
            dto.set_element6(element)  
        elif count == 7:
            dto.set_element7(element) 
        elif count == 8:
            dto.set_element8(element) 
        elif count == 9:
            dto.set_element9(element)  
        elif count == 10:
            dto.set_element10(element)    
        elif count == 11:
            dto.set_element11(element)    
        elif count == 12:
            dto.set_element12(element)    
        elif count == 13:
            dto.set_element13(element)  
        elif count == 14:
            dto.set_element14(element)  
        elif count == 15:
            dto.set_element15(element) 
        elif count == 16:
            dto.set_element16(element) 
        elif count == 17:
            dto.set_element17(element)  
        elif count == 18:
            dto.set_element18(element)
        elif count == 19:
            dto.set_element19(element)  
        elif count == 20:
            dto.set_element20(element)  
        elif count == 21:
            dto.set_element21(element)  
        elif count == 22:
            dto.set_element22(element)  
        elif count == 23:
            dto.set_element23(element)      
        elif count == 24:
            dto.set_element24(element)                
        elif count == 25:
            dto.set_element25(element)              
        elif count == 26:
            dto.set_element26(element)              
        elif count == 27:
            dto.set_element27(element)   
        elif count == 28:
            dto.set_element28(element) 
        elif count == 29:
            dto.set_element29(element)        
                
        
