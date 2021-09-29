import pandas
import time

def table():
    
    # today's USD exchange rate trend
    url = 'https://www.fubon.com/Fubon_Portal/banking/Personal/deposit/exchange_rate/exchange_rate1_photo.jsp?urlParameter=1D&currency=USD'
    pd = pandas.read_html(url)
    currency = pd[0] 
    return currency

def show_buy_table(buy_price): 
    temp = currency[0:1][['銀行賣出']].values
    if temp <= buy_price:
        print('BUY USD NOW')
        print('The price is :', float(temp))
        print('\n')
    else:
        print('You still need to wait...\n')
 
def show_sell_table(sell_price):     
    temp = currency[0:1][['銀行買入']].values
    if temp >= sell_price:
        print('SELL USD NOW')
        print('The price is :', float(temp))
        print('\n')
    else:
        print('You still need to wait...\n')
    
def service_costermus():
    
    tag = input('Buy USD(1))，Sell USD(2), None(3)\n')
    
    if tag == '1':
        service = 1
        return service
    elif tag == '2':
        service = 2
        return service
    else:
        service = 3
        return service
    
def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec


if __name__ == '__main__':

    
    delaytime = sleeptime(0,1,0)
    
    while True:
        
        # update the table when you try to type your price
        currency = table()
        print('|||Current Rate|||')
        print(currency)
        service = service_costermus()
    
        # buy
        if service == 1: 
            buy_price = input('The lowest price that you want to BUY:\n')
            show_buy_table(float(buy_price))
                 
        # sell  
        elif service == 2:    
            sell_price = input('The highest price that you want to SELL\n')
            show_sell_table(float(sell_price))
        
        # none
        else:
            break;
            
        print('############################')